#!/usr/bin/env python3
"""
maintain.py: the routine that runs after any wave changes.

1. classify every counter into a control class if unclassified
2. regenerate counters/COUNTERS.md as the defender facing view
3. update waves/QUEUE.json status and counts from what is actually on disk
4. render every wave

Idempotent. Safe to run any number of times. Never invents a count.
"""
import json, glob, sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WAVES = ROOT / "waves"
CC_FILE = ROOT / "data" / "control-classes.json"

RULES = [
    ("C01", ["object level", "ownership", "owner consent", "authorise the parent", "authorise both",
             "authorise restore", "authorise each", "authorise every", "per object"]),
    ("C02", ["function level", "route group", "role", "permission", "scope check", "admin only",
             "separation of duties", "policy", "privilege", "authoris", "authoriz"]),
    ("C03", ["allowlist", "binding", "field mask", "field level ownership", "resolver", "schema is not",
             "escape", "sanitis", "sanitiz", "encoding", "strip", "neutralis", "neutraliz", "one parser"]),
    ("C04", ["normalis", "canonical", "exact match", "identifier charset", "identity", "case", "collation", "bind"]),
    ("C05", ["state machine", "idempotency", "invariant", "three states", "validate at every", "sign and range",
             "bounded", "eligibility", "immutable", "snapshot", "tombstone", "propagat", "transactional",
             "conditional write", "outbox", "unique constraint"]),
    ("C06", ["single use", "refresh", "token", "credential", "audience", "mutual auth", "consent",
             "revocation", "purpose bound", "short lived"]),
    ("C07", ["parser", "duplicate", "typed binding", "reject", "content type", "sniff", "strict enum"]),
    ("C08", ["path", "containment", "destination", "canonicalis"]),
    ("C09", ["cache", "key", "ttl", "validator"]),
    ("C10", ["cost", "quota", "rate", "resource", "limit", "coalesce"]),
    ("C11", ["log", "audit", "attribution", "viewer"]),
    ("C12", ["version", "legacy", "decommission", "policy proxy", "retire"]),
]


def classify(mech):
    s = mech.lower()
    for cid, keys in RULES:
        if any(k in s for k in keys):
            return cid
    return "C02"


def load():
    rows, files = [], {}
    for f in sorted(WAVES.glob("*/patterns.jsonl")):
        items = [json.loads(l) for l in f.read_text(encoding="utf-8").splitlines() if l.strip()]
        files[f] = items
        rows.extend(items)
    return rows, files


def main():
    cc = json.load(open(CC_FILE))
    rows, files = load()

    changed = 0
    for f, items in files.items():
        dirty = False
        for p in items:
            if "control_class" not in p["counter"]:
                p["counter"]["control_class"] = classify(p["counter"]["mechanism"])
                dirty = True
                changed += 1
        if dirty:
            f.write_text("\n".join(json.dumps(p, ensure_ascii=False) for p in items) + "\n")

    by = defaultdict(list)
    for r in rows:
        by[r["counter"]["control_class"]].append(r)

    L = ["# Counters by control class", "",
         "A defender picks the classes they own and sees how many atlas patterns that closes. A researcher",
         "reads it the other way: this is what will stop you.", "",
         f"`{len(rows)}` patterns across `{len(by)}` control classes.", "",
         "| class | control | patterns closed |", "|---|---|---|"]
    for cid, ps in sorted(by.items(), key=lambda kv: -len(kv[1])):
        L.append(f"| {cid} | {cc['classes'][cid]['name']} | {len(ps)} |")
    L.append("")
    for cid, ps in sorted(by.items(), key=lambda kv: -len(kv[1])):
        L.append(f"## {cid}: {cc['classes'][cid]['name']}")
        L.append("")
        L.append(cc["classes"][cid]["desc"])
        L.append("")
        for p in sorted(ps, key=lambda x: x["id"]):
            L.append(f"- `{p['id']}` {p['title']}")
            L.append(f"  - counter: {p['counter']['mechanism']}")
        L.append("")
    (ROOT / "counters" / "COUNTERS.md").write_text("\n".join(L) + "\n")

    counts = Counter(r["_wave"] for r in rows if "_wave" in r) if False else {}
    counts = Counter()
    for f, items in files.items():
        counts[f.parent.name] = len(items)

    q = json.load(open(WAVES / "QUEUE.json"))
    for d in q["domains"]:
        n = counts.get(d["id"], 0)
        d["patterns"] = n
        if n == 0:
            d["status"] = "QUEUED"
        elif d["status"] != "DONE":
            d["status"] = "DONE" if n >= 50 else "PARTIAL"
    json.dump(q, open(WAVES / "QUEUE.json", "w"), indent=1)

    c = Counter(r["counter"]["control_class"] for r in rows)
    json.dump({"generated_at": "2026-10-26", "classes": cc["classes"], "pattern_counts": dict(c)},
              open(CC_FILE, "w"), indent=1)

    print(f"classified {changed} new counters")
    print(f"{len(rows)} patterns, {len(by)} control classes")
    for cid, ps in sorted(by.items(), key=lambda kv: -len(kv[1])):
        print(f"  {cid} {cc['classes'][cid]['name']:34s} {len(ps)}")
    done = [d["id"] for d in q["domains"] if d["status"] == "DONE"]
    print(f"\nwaves done: {', '.join(done) or 'none'}")
    print(f"queued: {sum(1 for d in q['domains'] if d['status']=='QUEUED')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
