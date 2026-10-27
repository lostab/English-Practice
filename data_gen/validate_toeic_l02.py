import json

with open("D:/work/Hermes/testprep-app/data_gen/output/toeic-l_02.json", encoding="utf-8") as f:
    data = json.load(f)

questions = data.get("questions", [])
print(f"Loaded {len(questions)} questions")

# Check IDs
ids = [q["id"] for q in questions]
expected_ids = [f"toeic-l-{i:03d}" for i in range(76, 97)]
if ids == expected_ids:
    print("✓ IDs are sequential and complete")
else:
    print("✗ ID mismatch:", ids)
    print("Expected:", expected_ids)

# Check word counts and roles
errors = []
for q in questions:
    qid = q["id"]
    words = q["audio"].split()
    wc = len(words)
    if not (90 <= wc <= 160):
        errors.append((qid, f"word count {wc} not in [90,160]"))
    # Check two roles: look for "Role:" pattern at line starts
    lines = q["audio"].split("\n") if "\n" in q["audio"] else q["audio"].split(".")
    roles = []
    for line in lines:
        if ":" in line:
            role = line.split(":", 1)[0].strip()
            roles.append(role)
    if len(set(roles)) < 2:
        errors.append((qid, f"less than 2 roles: {roles}"))
    # Options
    opts = q["options"]
    if len(opts) != 4:
        errors.append((qid, f"option count {len(opts)}"))
    elif len(set(opts)) != 4:
        errors.append((qid, "duplicate options"))
    # Answer
    ans = q["answer"]
    if not (0 <= ans <= 3):
        errors.append((qid, f"invalid answer {ans}"))
    # Explanation length
    expl = q["explanation"]
    if len(expl) > 90:
        errors.append((qid, f"explanation length {len(expl)}"))

if errors:
    print("\nErrors:")
    for qid, msg in errors:
        print(f"{qid}: {msg}")
else:
    print("\n✓ All checks passed")
    # Summary
    dist = {i: sum(1 for q in questions if q["answer"] == i) for i in range(4)}
    print("Answer distribution:", dist)
    print("Sample questions and word counts:")
    for q in questions[:3]:
        print(f"{q['id']}: {len(q['audio'].split())} words, roles: {[l.split(':',1)[0] for l in q['audio'].replace('\\n','\\n').split('\\n') if ':' in l]}")