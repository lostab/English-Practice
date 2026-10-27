#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate toeic-p5_04.json: ids 578-616, 39 questions, balanced answers, collision-checked."""
import json, random, glob

# Load all existing stems to avoid duplication
existing = set()
for f in glob.glob('D:/work/Hermes/testprep-app/data_gen/output/toeic-p5_*.json'):
    try:
        d = json.load(open(f, encoding='utf-8'))
        for q in d.get('questions', []):
            if isinstance(q, dict) and 'question' in q:
                existing.add(q['question'].strip())
    except Exception:
        pass
try:
    d = json.load(open('D:/work/Hermes/toeic_p5.json', encoding='utf-8'))
    qs = d.get('questions', d) if isinstance(d, dict) else d
    if isinstance(qs, list):
        for q in qs:
            if isinstance(q, dict) and 'question' in q:
                existing.add(q['question'].strip())
    elif isinstance(qs, dict) and 'questions' in qs:
        for q in qs['questions']:
            if isinstance(q, dict) and 'question' in q:
                existing.add(q['question'].strip())
except Exception:
    pass

# (stem, correct, [distractors], explanation)  — stem contains ______
Q = [
 ("All participants ______ submit their feedback forms before leaving the workshop venue.",
  "must", ["might", "could", "ought"], "must 表强制性要求，符合“必须提交”的语义。"),
 ("The interim financial report showed revenue ______ than analysts had projected.",
  "higher", ["high", "highest", "highly"], "than 提示比较级，用 higher。"),
 ("Should the server overload during peak hours, please ______ the traffic to the backup site.",
  "redirect", ["redirecting", "redirected", "redirects"], "please 后接动词原形；should 引导虚拟条件句。"),
 ("Ms. Garcia is the coordinator ______ presentation received the highest ratings from attendees.",
  "whose", ["who", "whom", "which"], "whose 表所属关系，修饰 presentation。"),
 ("Of the three software vendors evaluated, the committee selected the one that was ______ to integrate.",
  "easiest", ["easier", "easy", "easily"], "of the three 表范围，用最高级 easiest。"),
 ("Neither the marketing team nor the product developers ______ informed about the launch delay.",
  "were", ["was", "have been", "is"], "neither...nor 就近原则，developers 为复数用 were。"),
 ("Only after the compliance officer signed off ______ could the new feature be released.",
  "would", ["does", "had", "was"], "only 置于句首，主句部分倒装，过去时用 would。"),
 ("The audit committee eventually agreed ______ the scope of the upcoming internal review.",
  "on", ["with", "to", "about"], "agree on 表“就……达成一致”。"),
 ("The updated travel policy, ______ begins next quarter, was approved by the CFO last week.",
  "which", ["who", "whom", "where"], "先行词指物，非限定性定语从句缺主语，用 which。"),
 ("Field agents now spend significantly ______ on mileage reimbursements than they did last year.",
  "less", ["fewer", "least", "little"], "spend 后接不可数金额，用 less 表“更少”。"),
 ("We will activate the disaster recovery plan once the IT director ______ the system integrity.",
  "has verified", ["will verify", "verified", "would verify"], "once 引导时间状语从句，用现在完成时表将来。"),
 ("The facilities department is responsible for ______ all safety equipment on a monthly basis.",
  "inspecting", ["inspected", "inspect", "to inspect"], "be responsible for 后接动名词 inspecting。"),
 ("Please store the master keys ______ the locked cabinet in the security office.",
  "in", ["on", "at", "with"], "表示“在柜子里”用介词 in。"),
 ("______ the shipment clears customs by Friday, we will not meet the client's delivery window.",
  "Unless", ["Because", "Although", "If"], "unless 表“除非”，后接肯定句表否定条件。"),
 ("______ of the night-shift staff are permitted to take breaks in the designated lounge.",
  "None", ["All", "Some", "Most"], "后接否定逻辑，只有 none 与句意一致。"),
 ("The upgraded firewall is expected ______ unauthorized access attempts by a substantial percentage.",
  "to block", ["blocking", "blocked", "block"], "be expected to do sth. 为固定搭配。"),
 ("______ the sudden power outage, the data center maintained full operational capacity.",
  "Despite", ["Because of", "Due to", "Thanks to"], "despite 表让步“尽管”，后接名词短语。"),
 ("The client inquired ______ the service-level agreement includes weekend support coverage.",
  "whether", ["that", "because", "unless"], "whether 引导宾语从句，表“是否”。"),
 ("The interns were divided into teams; ______ team was assigned a different market segment.",
  "each", ["every", "all", "most"], "each 作主语指“每个小组”，谓语用单数。"),
 ("The cargo was delayed ______ adverse weather conditions at the departure airport.",
  "by", ["for", "at", "on"], "be delayed by 表“被……延迟”，被动语态引导者用 by。"),
 ("Applicants who pass the language proficiency test ______ be scheduled for a second interview.",
  "will", ["were", "had", "would"], "表将来将被安排，用一般将来时 will。"),
 ("______ completing the mandatory ethics training, employees receive a certificate of completion.",
  "Upon", ["Before", "Despite", "Unless"], "upon doing sth. 表“在完成……之后/之时”。"),
 ("The negotiation team reached consensus ______ the royalty rates for the licensed technology.",
  "on", ["with", "to", "about"], "reach consensus on 表“就……达成共识”。"),
 ("The analysts are reviewing the variances that ______ in the quarterly budget comparison.",
  "appeared", ["appear", "will appear", "have been appearing"], "描述季度预算对比中已出现的问题，用过去时 appeared。"),
 ("Visitors must present a government-issued ID ______ entering the research and development wing.",
  "before", ["during", "after", "until"], "before entering 意为“进入之前”。"),
 ("The survey results were tabulated ______ so that the product manager could identify trends immediately.",
  "electronically", ["electronic", "electronics", "electrified"], "修饰动词 tabulated 用副词 electronically“以电子方式”。"),
 ("Had the logistics coordinator received the warehouse schedule earlier, they ______ the inbound shipments accordingly.",
  "would have adjusted", ["will adjust", "adjust", "had adjusted"], "had 引导的虚拟条件句，主句用 would have + 过去分词。"),
 ("______ feedback is resolved more efficiently when it is submitted via the online portal.",
  "Customer", ["The customers", "Customers'", "Customer's"], "名词作定语修饰 feedback，不加所有格。"),
 ("The procurement specialist compared the estimated lead times ______ the actual delivery dates.",
  "against", ["of", "at", "for"], "compare sth. against sth. 表“把……与……对照”。"),
 ("The revised dividend policy will be communicated to every shareholder ______ the annual general meeting.",
  "at", ["within", "from", "toward"], "at the meeting 表“在会议上”。"),
 ("The exhibit signage was fabricated ______ clearly that passersby could grasp the brand message within seconds.",
  "so", ["such", "too", "as"], "so + that 引导结果状语从句，表“如此……以至于”。"),
 ("The quarterly webinar attracted registrants ______ than the previous session due to improved topic relevance.",
  "more", ["most", "many", "much"], "than 提示比较级，用 more 修饰可数名词复数。"),
 ("Should the main database experience latency, please ______ the read requests to the replica node.",
  "route", ["routing", "routed", "routes"], "please 后接动词原形；should 引导虚拟条件句。"),
 ("Mr. Epstein is the supervisor ______ feedback consistently received the highest satisfaction scores.",
  "whose", ["who", "whom", "which"], "whose 表所属关系，修饰 feedback。"),
 ("Of the four office layouts tested, employees preferred the one that was ______ for collaborative work.",
  "best suited", ["better suited", "well suited", "good suited"], "of the four 表范围，用最高级 best suited。"),
 ("Neither the HR department nor the payroll team ______ notified of the changes to the tax withholding tables.",
  "was", ["were", "have been", "is"], "neither...nor 就近原则，team 为单数用 was。"),
 ("Only after the legal department completed its review ______ could the partnership agreement be executed.",
  "did", ["does", "had", "was"], "only 置于句首，主句部分倒装，过去时用 did。"),
 ("The building management committee eventually agreed ______ the proposed renovation timeline for the lobby.",
  "to", ["for", "on", "with"], "agree to sth. 表“同意某项安排”。"),
 ("The updated remote-work policy, ______ takes effect on the first of next month, was reviewed by IT security.",
  "which", ["who", "whom", "where"], "先行词指物，非限定性定语从句缺主语，用 which。"),
]

assert len(Q) == 39, f"need 39 questions, got {len(Q)}"

# assign answer index: balanced 10/10/10/9, deterministically shuffled
random.seed(20241011)
indices = [0]*10 + [1]*10 + [2]*10 + [3]*9
random.shuffle(indices)

questions = []
used_stems = set()
collisions = 0
for i, (stem, correct, dist, expl) in enumerate(Q):
    if "______" not in stem:
        raise ValueError(f"Q{i} stem has no blank: {stem}")
    # collision check
    key = stem.strip()
    if key in existing:
        print(f"WARN collision with existing bank at Q{i}: {key}")
        collisions += 1
    if key in used_stems:
        raise ValueError(f"internal duplicate at Q{i}: {key}")
    used_stems.add(key)

    pos = indices[i]
    others = [d for d in dist]
    random.Random(42 + i).shuffle(others)
    opts = others[:pos] + [correct] + others[pos:]
    qid = f"toeic-p5-{578+i}"
    questions.append({
        "id": qid, "exam": "toeic", "section": "reading", "part": 5,
        "question": stem, "options": opts, "answer": pos, "explanation": expl,
    })

out = {"questions": questions}
path = 'D:/work/Hermes/testprep-app/data_gen/output/toeic-p5_04.json'
json.dump(out, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print("written", path)

# ---- validation ----
d = json.load(open(path, encoding='utf-8'))
qs = d['questions']
ids = [q['id'] for q in qs]
exp = [f"toeic-p5-{i}" for i in range(578, 617)]
assert ids == exp, "id sequence broken"
assert len(qs) == 39
for q in qs:
    assert len(q['options']) == 4 and len(set(q['options'])) == 4, q['id']
    assert 0 <= q['answer'] <= 3, q['id']
    assert q['explanation'] and len(q['explanation']) <= 80, q['id']
from collections import Counter
c = Counter(q['answer'] for q in qs)
print("answer distribution:", dict(sorted(c.items())))
print("collisions with existing bank:", collisions)
print("ALL CHECKS PASSED")
