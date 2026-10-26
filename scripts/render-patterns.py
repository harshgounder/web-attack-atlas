#!/usr/bin/env python3
"""
render-patterns.py: gate check plus markdown render for atlas patterns.

The gate is the point of this repo. A pattern ships only when it answers:
  1. what state changes      (target_state)
  2. as whom                 (principal)
  3. does it persist         (persistence)
  4. how do you know         (oracle + negative_control)
  5. what stops it           (counter)

Usage:
  python3 scripts/render-patterns.py --check        # gate only, exit 1 on failure
  python3 scripts/render-patterns.py --render       # gate plus markdown
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WAVES = ROOT / "waves"
OUT = ROOT / "patterns"

REQUIRED = ["id", "title", "atom", "target_state", "principal", "persistence",
            "preconditions", "oracle", "negative_control", "counter", "authorization", "status"]

ATOM_NAMES = json.load(open(ROOT / "data" / "atoms.json"))
ATOMS = {a["id"]: a["name"] for a in ATOM_NAMES["atoms"]}


def load():
    rows = []
    for f in sorted(WAVES.glob("*/patterns.jsonl")):
        for line in f.read_text(encoding="utf-8", errors="replace").splitlines():
            if line.strip():
                p = json.loads(line)
                p["_wave"] = f.parent.name
                rows.append(p)
    return rows


def gate(rows):
    failures = []
    for p in rows:
        missing = [k for k in REQUIRED if not p.get(k)]
        if missing:
            failures.append((p.get("id", "?"), f"missing fields: {', '.join(missing)}"))
            continue
        c = p["counter"]
        if not isinstance(c, dict) or not c.get("mechanism"):
            failures.append((p["id"], "counter has no mechanism"))
        if not p.get("mutations"):
            failures.append((p["id"], "no mutations"))
        if p.get("status") not in ("VERIFIED", "PROBABLE", "DRAFT"):
            failures.append((p["id"], f"bad status {p.get('status')}"))
    return failures


def render(rows):
    by_wave = {}
    for p in rows:
        by_wave.setdefault(p["_wave"], []).append(p)
    OUT.mkdir(exist_ok=True)
    queue = json.load(open(WAVES / "QUEUE.json"))
    titles = {d["id"]: d["title"] for d in queue["domains"]}
    for wave, ps in by_wave.items():
        ps.sort(key=lambda x: x["id"])
        L = []
        a = L.append
        a(f"# {wave}: {titles.get(wave, wave)}")
        a("")
        a(f"Generated from `waves/{wave}/patterns.jsonl`. Do not edit by hand.")
        a(f"{len(ps)} patterns. Every one answers the five questions and carries a counter.")
        a("")
        a("## Index")
        a("")
        a("| id | pattern | atoms | persists | counter mechanism |")
        a("|---|---|---|---|---|")
        for p in ps:
            atoms = ", ".join(p["atom"])
            a(f"| {p['id']} | {p['title']} | {atoms} | {p['persistence']} | {p['counter']['mechanism']} |")
        a("")
        for p in ps:
            a(f"## {p['id']}: {p['title']}")
            a("")
            a(f"**Atoms:** {', '.join(f'`{x}` {ATOMS.get(x, '')}' for x in p['atom'])}  ")
            a(f"**State changed:** {p['target_state']}  ")
            a(f"**Acting as:** {p['principal']}  ")
            a(f"**Persistence:** {p['persistence']}  ")
            a(f"**Status:** {p['status']}  ")
            a(f"**Authorization:** {p['authorization']}")
            a("")
            a("Preconditions:")
            for x in p["preconditions"]:
                a(f"- {x}")
            a("")
            a("Procedure:")
            for i, x in enumerate(p["procedure"], 1):
                a(f"{i}. {x}")
            a("")
            a(f"**Oracle:** {', '.join('`'+o+'`' for o in p['oracle'])}  ")
            a(f"**Negative control:** {p['negative_control']}")
            a("")
            if p.get("mutations"):
                a("| mutation axis | variant | why it matters |")
                a("|---|---|---|")
                for m in p["mutations"]:
                    a(f"| {m['axis']} | `{m['variant']}` | {m['why']} |")
                a("")
            if p.get("detected_by"):
                a(f"**Detected by:** {', '.join(p['detected_by'])}")
                a("")
            c = p["counter"]
            a(f"**Counter:** {c['mechanism']}  ")
            a(f"**Counter precondition:** {c.get('precondition','')}  ")
            a(f"**Counter cost:** {c.get('cost','')}")
            a("")
            if p.get("tools"):
                a(f"**Tools (resolve in ai-web-arsenal):** {', '.join('`'+t+'`' for t in p['tools'])}")
                a("")
            a("---")
            a("")
        (OUT / f"{wave}-{titles.get(wave, wave).replace(' ', '-')}.md").write_text("\n".join(L))
        print(f"rendered {wave}: {len(ps)} patterns")


def main():
    rows = load()
    fails = gate(rows)
    print(f"patterns loaded: {len(rows)}")
    if fails:
        print(f"GATE FAILURES: {len(fails)}")
        for pid, why in fails:
            print(f"  {pid}: {why}")
        if "--check" in sys.argv:
            return 1
    else:
        print("gate: all pass")
    if "--render" in sys.argv:
        render(rows)
    # coverage vs the declared bar
    queue = json.load(open(WAVES / "QUEUE.json"))
    counts = {}
    for p in rows:
        counts[p["_wave"]] = counts.get(p["_wave"], 0) + 1
    print("\nbar per domain:", queue["bar"])
    for d in queue["domains"]:
        n = counts.get(d["id"], 0)
        state = "done" if n >= 50 else ("partial" if n else "queued")
        print(f"  {d['id']} {d['title'][:38]:38s} {n:3d}  {state}")
    return 1 if fails and "--check" in sys.argv else 0


if __name__ == "__main__":
    sys.exit(main())
