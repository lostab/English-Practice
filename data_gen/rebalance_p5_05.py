import json

path = r"D:\work\Hermes\testprep-app\data_gen\output\toeic-p5_05.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

questions = data["questions"]

# Rebalance: current distribution {0:8, 1:6, 2:8, 3:17} -> target {0:10, 1:10, 2:10, 3:9}
# Move 8 questions from index 3: 2 to index 0, 4 to index 1, 2 to index 2.
targets = [0, 0, 1, 1, 1, 1, 2, 2]
moved = 0
for q in questions:
    if q["answer"] == 3 and moved < len(targets):
        target = targets[moved]
        opts = q["options"]
        correct = opts[3]
        # rebuild options with the correct answer at `target`, keeping others' order
        rest = [o for o in opts if o != correct]
        new_opts = rest[:target] + [correct] + rest[target:]
        assert sorted(new_opts) == sorted(opts) and len(set(new_opts)) == 4
        q["options"] = new_opts
        q["answer"] = target
        moved += 1

assert moved == 8, f"expected 8 moves, did {moved}"

# Full validation
assert len(questions) == 39
ids = [q["id"] for q in questions]
assert ids == [f"toeic-p5-{i}" for i in range(617, 656)], "ID range broken"
for q in questions:
    assert len(q["options"]) == 4 and len(set(q["options"])) == 4
    assert 0 <= q["answer"] <= 3
    assert q["options"][q["answer"]] in q["options"]
    assert len(q["explanation"]) <= 80

dist = {i: [q["answer"] for q in questions].count(i) for i in range(4)}
print("Answer distribution:", dist)

with open(path, "w", encoding="utf-8") as f:
    json.dump({"questions": questions}, f, ensure_ascii=False, indent=2)

# quick sanity print of the rebalanced questions
for q in questions:
    print(q["id"], "A" if q["answer"] == 0 else "B" if q["answer"] == 1 else "C" if q["answer"] == 2 else "D",
          "|", q["options"][q["answer"]])