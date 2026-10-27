import json
import re

path = "D:/work/Hermes/testprep-app/data_gen/output/toeic-l_02.json"

with open(path, encoding="utf-8") as f:
    data = json.load(f)

print("=== TOEIC-L_02 FULL VALIDATION ===\n")

issues = []

# 1. Basic structure
if not isinstance(data, dict):
    issues.append("Root is not an object")
if "questions" not in data:
    issues.append("Missing 'questions' key")
    data = {"questions": []}
questions = data["questions"]

n = len(questions)
print(f"1. Total questions: {n} (required 21) {'PASS' if n == 21 else 'FAIL'}")
if n != 21:
    issues.append(f"Question count is {n}, expected 21")

# 2. ID check: sequential toeic-l-076..toeic-l-096, no gaps/dupes
ids = [q["id"] for q in questions]
expected = [f"toeic-l-{i:03d}" for i in range(76, 97)]
if ids == expected:
    print(f"2. IDs sequential toeic-l-076..toeic-l-096: PASS")
else:
    print(f"2. IDs FAIL: actual={ids}")
    issues.append(f"ID sequence mismatch")

# 3. Unique ids
if len(set(ids)) == len(ids):
    print(f"3. No duplicate IDs: PASS")
else:
    issues.append("Duplicate IDs found")
    print(f"3. Duplicate IDs: FAIL")

# 4. Role count check
def get_roles(audio):
    sentences = [s.strip() for s in re.split(r"(?<=[.!?]) ", audio) if s.strip()]
    return [s.split(":", 1)[0] for s in sentences if ":" in s]

for q in questions:
    roles = get_roles(q["audio"])
    if len(set(roles)) < 2:
        issues.append(f"{q['id']}: fewer than 2 roles ({roles})")
        print(f"{q['id']}: FAIL - fewer than 2 roles: {roles}")

role_counts = {qid: len(set(get_roles(q["audio"]))) for qid, q in zip(ids, questions)}
print(f"4. Each audio has >=2 distinct roles: PASS ({'all good' if len(set(role_counts.values()) >= 2 and all(v>=2 for v in role_counts.values())) else 'see above'})")

# 5. Word count 90-160
wc_bad = [(q["id"], len(q["audio"].split())) for q in questions if not (90 <= len(q["audio"].split()) <= 160)]
if not wc_bad:
    print("5. Audio word count 90-160: PASS")
else:
    print(f"5. Word count FAIL: {wc_bad}")
    issues.extend(f"{i}: {w} words" for i, w in wc_bad)

# 6. Options: exactly 4, distinct
opt_bad = [(q["id"], len(q["options"]), len(set(q["options"]))) for q in questions if len(q["options"]) != 4 or len(set(q["options"])) != 4]
if not opt_bad:
    print("6. Options: exactly 4 distinct: PASS")
else:
    print(f"6. Options FAIL: {opt_bad}")
    issues.extend(f"{i}: {o}" for i, o in opt_bad)

# 7. Answer: int 0-3
ans_bad = [(q["id"], q["answer"]) for q in questions if not (isinstance(q["answer"], int) and 0 <= q["answer"] <= 3)]
if not ans_bad:
    print("7. Answer int 0-3: PASS")
else:
    print(f"7. Answer FAIL: {ans_bad}")
    issues.extend(f"{i}: {a}" for i, a in ans_bad)

# 8. Explanation: non-empty, <= 90 chars
expl_bad = [(q["id"], len(q["explanation"])) for q in questions if not (0 < len(q["explanation"]) <= 90)]
if not expl_bad:
    print("8. Explanation <=90 chars: PASS")
else:
    print(f"8. Explanation FAIL: {expl_bad}")
    issues.extend(f"{i}: {e} chars" for i, e in expl_bad)

# 9. Exam/section/part consistency
cons_bad = [(q["id"], q.get("exam"), q.get("section"), q.get("part")) for q in questions if q.get("exam") != "toeic" or q.get("section") != "listening" or q.get("part") != 2]
if not cons_bad:
    print("9. exam=toeic, section=listening, part=2: PASS")
else:
    print(f"9. Consistency FAIL: {cons_bad}")
    issues.extend(f"{i}: {c}" for i, c in cons_bad)

# 10. Answer distribution
dist = {i: sum(1 for q in questions if q["answer"] == i) for i in range(4)}
print(f"\n=== Answer distribution ===")
for i in range(4):
    print(f"  Answer {i}: {dist[i]}")
total = sum(dist.values())
max_imbalance = max(dist.values()) - min(dist.values())
imbalance_ok = max_imbalance <= 3
print(f"\nMin-max imbalance: {max_imbalance} ({'OK' if imbalance_ok else 'high'})")

# 11. Question stem ends with ?
stem_bad = [q["id"] for q in questions if not (isinstance(q["question"], str) and q["question"].endswith("?"))]
if not stem_bad:
    print("10. Question stems end with '?': PASS")
else:
    print(f"10. Stem FAIL: {stem_bad}")
    issues.extend(f"{i}" for i in stem_bad)

# 12. Roles named (capitalized at turn start)
role_names = {}
for q in questions:
    roles = get_roles(q["audio"])
    role_names.setdefault(q["id"], set()).update(roles)

# 13. No empty fields
fields = ["audio", "question", "explanation"]
empty_bad = [q["id"] for q in questions if any(not q.get(f) for f in fields)]
if not empty_bad:
    print("11. No empty required fields: PASS")
else:
    print(f"11. Empty fields FAIL: {empty_bad}")
    issues.extend(f"{i}" for i in empty_bad)

print("\n=== RESULT ===")
if issues:
    print("ISSUES FOUND:")
    for i in issues:
        print(f"  - {i}")
else:
    print("ALL CHECKS PASSED!")

# Print sample rows
print("\n=== SAMPLE (first 3) ===")
for q in questions[:3]:
    print(f"- {q['id']} | ans={q['answer']} | roles={sorted(set(get_roles(q['audio'])))} | wc={len(q['audio'].split())}")
    print(f"    q: {q['question']}")
    print(f"    opts: {q['options']}")
    print(f"    expl: {q['explanation']}")