#!/usr/bin/env python3
"""Run one validation scenario: agent under test vs. simulated user, then an evaluator.

    python tests/harness/run_scenario.py <scenario-name> [--max-turns N] [--keep]

Layout of tests/scenarios/<name>/:
    scenario.json   opening prompt, turn cap, deterministic checks
    persona.md      who the simulated user is and how they behave
    rubric.md       judgment items for the evaluator
    fixture/        seed contents for the sandbox's personal-untracked/ (fictional persona)

Everything runs in a throwaway sandbox copy of the repo, never in the real working tree, and
never against the real personal-untracked/. Uses only the `claude` CLI (print mode).
"""

import argparse
import fnmatch
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
import uuid
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SCENARIOS = REPO / "tests" / "scenarios"
RUNS = REPO / "tests" / "runs"
CLAUDE = shutil.which("claude") or "claude"

# Repo content copied into the sandbox. personal-untracked/ and .git are deliberately absent.
COPY_ITEMS = [".claude", "templates", "habits", "context", "CLAUDE.md", "README.md", "ONBOARDING.md"]
SKIP_IN_CLAUDE_DIR = {"settings.json", "settings.local.json"}

AGENT_TOOLS = ["Read", "Write", "Edit", "Glob", "Grep", "Skill", "Bash(date:*)", "Bash(ls:*)"]
SANDBOX_NOTE = (
    "You are running inside an automated test sandbox. Todoist, Google Calendar and Slack MCP "
    "servers are NOT available: where a command says to sync with them, say they are "
    "unavailable and continue with local files only. Otherwise follow the repository's command "
    "files exactly as you normally would. Today's date is {today}."
)
SIM_USER_SYSTEM = (
    "You are role-playing a human user in a conversation with an AI assistant, for software "
    "testing. Stay strictly in character as described in the persona. Reply with ONLY the "
    "user's next message, in the persona's voice, no stage directions, no quotes. Answer what "
    "the assistant actually asked; do not volunteer everything at once. If the conversation has "
    "reached a natural end (the assistant has wrapped up and nothing more is needed), reply with "
    "exactly [END]."
)
EVAL_SCHEMA = {
    "type": "object",
    "properties": {
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "verdict": {"type": "string", "enum": ["pass", "fail", "n/a"]},
                    "evidence": {"type": "string"},
                    "note": {"type": "string"},
                },
                "required": ["id", "verdict", "evidence"],
            },
        },
        "summary": {"type": "string"},
    },
    "required": ["items", "summary"],
}


def run_claude(args, prompt, cwd, timeout=900):
    """Run `claude -p` and return the parsed JSON result."""
    proc = subprocess.run(
        [CLAUDE, "-p", *args, "--output-format", "json"],
        input=prompt, capture_output=True, text=True, encoding="utf-8",
        cwd=cwd, timeout=timeout,
    )
    try:
        data = json.loads(proc.stdout)
    except json.JSONDecodeError:
        raise RuntimeError(f"claude returned non-JSON (exit {proc.returncode}):\n{proc.stdout}\n{proc.stderr}")
    if data.get("is_error"):
        raise RuntimeError(f"claude error: {data.get('result')}")
    return data


def git(sandbox, *args):
    return subprocess.run(
        ["git", "-c", "user.name=harness", "-c", "user.email=h@example.invalid", *args],
        cwd=sandbox, capture_output=True, text=True, encoding="utf-8",
    ).stdout


def build_sandbox(scenario_dir, scenario):
    sandbox = Path(tempfile.mkdtemp(prefix="gtd-sandbox-"))
    for item in COPY_ITEMS:
        src = REPO / item
        if not src.exists():
            continue
        dst = sandbox / item
        if src.is_dir():
            ignore = (lambda d, names: [n for n in names if n in SKIP_IN_CLAUDE_DIR]) if item == ".claude" else None
            shutil.copytree(src, dst, ignore=ignore)
        else:
            shutil.copy2(src, dst)
    fixture = SCENARIOS / scenario.get("fixture_from", scenario_dir.name) / "fixture"
    if fixture.exists():
        shutil.copytree(fixture, sandbox / "personal-untracked")
    # personal-untracked/ is gitignored in the real repo; the sandbox needs it tracked so
    # `git diff` can show exactly what the agent changed.
    git(sandbox, "init", "-q")
    git(sandbox, "add", "-A")
    git(sandbox, "commit", "-q", "-m", "baseline")
    return sandbox


def agent_turn(sandbox, session_id, message, first, today, budget):
    args = [
        "--permission-mode", "acceptEdits",
        "--allowedTools", *AGENT_TOOLS,
        "--disallowedTools", "WebFetch", "WebSearch",
        "--setting-sources", "project",
        "--append-system-prompt", SANDBOX_NOTE.format(today=today),
        "--max-budget-usd", str(budget),
    ]
    args += ["--session-id", session_id] if first else ["--resume", session_id]
    return run_claude(args, message, sandbox)


def render(transcript):
    return "\n\n".join(f"{'USER' if who == 'user' else 'ASSISTANT'}: {text}" for who, text in transcript)


def sim_user_turn(persona, transcript, scratch):
    prompt = (
        f"# Persona\n\n{persona}\n\n# Conversation so far\n\n{render(transcript)}\n\n"
        "# Your task\n\nWrite the user's next message (or [END])."
    )
    args = ["--tools", "", "--no-session-persistence", "--setting-sources", "",
            "--system-prompt", SIM_USER_SYSTEM]
    return run_claude(args, prompt, scratch)["result"].strip()


def changed_files(sandbox):
    out = git(sandbox, "status", "--porcelain", "--untracked-files=all")
    files = {}
    for line in out.splitlines():
        status, path = line[:2].strip(), line[3:].strip().strip('"')
        files[path] = "added" if status in ("??", "A") else "deleted" if status == "D" else "modified"
    return files


def run_deterministic(sandbox, checks, changes):
    results = []
    for chk in checks:
        cid, kind = chk["id"], chk["type"]
        ok, detail = False, ""
        if kind == "file_unchanged":
            ok = chk["path"] not in changes
            detail = f"{chk['path']}: {changes.get(chk['path'], 'unchanged')}"
        elif kind == "file_changed":
            ok = chk["path"] in changes
            detail = f"{chk['path']}: {changes.get(chk['path'], 'unchanged')}"
        elif kind in ("file_contains", "file_not_contains"):
            path = sandbox / chk["path"]
            text = path.read_text(encoding="utf-8") if path.exists() else ""
            found = re.search(chk["pattern"], text, re.MULTILINE) is not None
            ok = found if kind == "file_contains" else not found
            detail = f"{chk['path']}: pattern {'found' if found else 'not found'}"
        elif kind == "only_changed":
            stray = [p for p in changes if not any(fnmatch.fnmatch(p, g) for g in chk["allowed"])]
            ok = not stray
            detail = f"unexpected changes: {stray}" if stray else "no unexpected changes"
        elif kind == "privacy_header_on_new":
            missing = []
            for p, st in changes.items():
                if st == "added" and p.startswith("personal-untracked/") and p.endswith(".md"):
                    head = (sandbox / p).read_text(encoding="utf-8")[:600]
                    if "> Private: this file is private user context" not in head:
                        missing.append(p)
            ok = not missing
            detail = f"new files missing privacy note: {missing}" if missing else "all new files have privacy note"
        else:
            detail = f"unknown check type {kind}"
        results.append({"id": cid, "verdict": "pass" if ok else "fail", "detail": detail,
                        "description": chk.get("description", "")})
    return results


def evaluate(scenario_dir, scenario, transcript, sandbox, det, scratch):
    rubric = (scenario_dir / "rubric.md").read_text(encoding="utf-8")
    diff = git(sandbox, "diff", "HEAD", "--", ".")
    untracked = [p for p, st in changed_files(sandbox).items() if st == "added"]
    for p in untracked:
        diff += f"\n\n--- NEW FILE {p} ---\n" + (sandbox / p).read_text(encoding="utf-8")
    prompt = (
        "You are a strict, evidence-based evaluator of an AI assistant's behavior in a test "
        "conversation. Judge ONLY against the rubric. For each rubric item return pass, fail, or "
        "n/a (if the situation never arose), with a short verbatim quote from the transcript or "
        "diff as evidence. Do not be generous: if the evidence is ambiguous, say fail and explain.\n\n"
        f"# Rubric\n\n{rubric}\n\n# Transcript\n\n{render(transcript)}\n\n"
        f"# File changes made in the sandbox (git diff)\n\n{diff or '(none)'}\n\n"
        f"# Deterministic check results (already computed)\n\n{json.dumps(det, indent=2)}\n"
    )
    args = ["--tools", "", "--no-session-persistence", "--setting-sources", "",
            "--json-schema", json.dumps(EVAL_SCHEMA)]
    data = run_claude(args, prompt, scratch)
    structured = data.get("structured_output")
    if structured is None:
        structured = json.loads(re.search(r"\{.*\}", data["result"], re.DOTALL).group(0))
    return structured, diff


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser()
    ap.add_argument("scenario")
    ap.add_argument("--max-turns", type=int)
    ap.add_argument("--keep", action="store_true", help="keep the sandbox directory afterwards")
    ap.add_argument("--budget", type=float, default=5.0, help="max USD per agent turn")
    opts = ap.parse_args()

    scenario_dir = SCENARIOS / opts.scenario
    scenario = json.loads((scenario_dir / "scenario.json").read_text(encoding="utf-8"))
    persona = (scenario_dir / "persona.md").read_text(encoding="utf-8")
    max_turns = opts.max_turns or scenario.get("max_turns", 12)
    today = scenario.get("today", time.strftime("%Y-%m-%d"))

    sandbox = build_sandbox(scenario_dir, scenario)
    scratch = Path(tempfile.mkdtemp(prefix="gtd-scratch-"))  # neutral cwd for sim-user/evaluator
    run_dir = RUNS / f"{opts.scenario}-{time.strftime('%Y%m%d-%H%M%S')}"
    run_dir.mkdir(parents=True, exist_ok=True)
    print(f"sandbox: {sandbox}\nrun dir: {run_dir}", flush=True)

    session_id = str(uuid.uuid4())
    transcript, user_msg, cost = [], scenario["opening_prompt"], 0.0
    for turn in range(max_turns):
        transcript.append(("user", user_msg))
        reply = agent_turn(sandbox, session_id, user_msg, turn == 0, today, opts.budget)
        cost += reply.get("total_cost_usd", 0) or 0
        transcript.append(("assistant", reply["result"]))
        print(f"turn {turn + 1} done", flush=True)
        user_msg = sim_user_turn(persona, transcript, scratch)
        if user_msg.strip() == "[END]" or not user_msg.strip():
            break

    changes = changed_files(sandbox)
    det = run_deterministic(sandbox, scenario.get("checks", []), changes)
    judged, diff = evaluate(scenario_dir, scenario, transcript, sandbox, det, scratch)

    (run_dir / "transcript.md").write_text(render(transcript), encoding="utf-8")
    (run_dir / "changes.diff").write_text(diff, encoding="utf-8")
    report = {"scenario": opts.scenario, "turns": len(transcript) // 2, "agent_cost_usd": round(cost, 4),
              "deterministic": det, "judged": judged}
    (run_dir / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")

    fails = [d for d in det if d["verdict"] == "fail"] + [i for i in judged["items"] if i["verdict"] == "fail"]
    print("\n== Deterministic ==")
    for d in det:
        print(f"[{d['verdict'].upper():4}] {d['id']} — {d['detail']}")
    print("\n== Judged ==")
    for i in judged["items"]:
        print(f"[{i['verdict'].upper():4}] {i['id']} — {i['evidence'][:160]}")
    print(f"\nsummary: {judged['summary']}\nreport: {run_dir / 'report.json'}")
    if not opts.keep:
        shutil.rmtree(sandbox, ignore_errors=True)
    shutil.rmtree(scratch, ignore_errors=True)
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
