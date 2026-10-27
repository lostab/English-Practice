import json
import os

questions = [
    {
        "id": "toeic-p5-617",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "The quarterly financial report has been delayed ______ the recent server outage.",
        "options": ["during", "due to", "despite", "unless"],
        "answer": 1,
        "explanation": "due to 表原因，后接名词短语，表示“由于”。"
    },
    {
        "id": "toeic-p5-618",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "All employees are required to submit ______ expense claims by Friday afternoon.",
        "options": ["they", "them", "their", "theirs"],
        "answer": 2,
        "explanation": "修饰名词 expense claims 需用形容词性物主代词 their。"
    },
    {
        "id": "toeic-p5-619",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "Mr. Harrison reviewed the blueprint ______ before approving the construction contract.",
        "options": ["careful", "carefully", "carefulness", "care"],
        "answer": 1,
        "explanation": "修饰动词 reviewed 需用副词 carefully。"
    },
    {
        "id": "toeic-p5-620",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "Ms. Jenkins will lead the marketing team ______ Mr. Davis is on maternity leave.",
        "options": ["while", "during", "despite", "because"],
        "answer": 0,
        "explanation": "引导时间状语从句表“在……期间”，应用连词 while。"
    },
    {
        "id": "toeic-p5-621",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "The newly developed software program is ______ of handling millions of transactions simultaneously.",
        "options": ["able", "capable", "suitable", "expert"],
        "answer": 1,
        "explanation": "be capable of 为固定搭配，意为“有能力……”。"
    },
    {
        "id": "toeic-p5-622",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "If the shipment ______ tomorrow, we will be able to launch the product on schedule.",
        "options": ["arrive", "arrived", "arrives", "will arrive"],
        "answer": 2,
        "explanation": "在条件状语从句中用一般现在时表将来，主语 shipment 为单数。"
    },
    {
        "id": "toeic-p5-623",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "The board of directors discussed several strategies to ______ overall operational costs.",
        "options": ["reduction", "reducing", "reduced", "reduce"],
        "answer": 3,
        "explanation": "动词不定式符号 to 后接动词原形 reduce 表目的。"
    },
    {
        "id": "toeic-p5-624",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "Participants who complete the training workshop will receive a certificate of ______.",
        "options": ["complete", "completed", "completion", "completely"],
        "answer": 2,
        "explanation": "介词 of 后接名词 completion 构成名词短语。"
    },
    {
        "id": "toeic-p5-625",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "Customers may return any defective merchandise within 30 days of purchase for a full ______.",
        "options": ["exchange", "discount", "receipt", "refund"],
        "answer": 3,
        "explanation": "for a full refund 意为“全额退款”，符合语境。"
    },
    {
        "id": "toeic-p5-626",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "To ensure data security, passwords must contain ______ eight characters.",
        "options": ["at most", "as well as", "at least", "as soon as"],
        "answer": 2,
        "explanation": "at least 意为“至少”，符合密码安全要求的语境。"
    },
    {
        "id": "toeic-p5-627",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "The director of human resources announced that the annual meeting ______ postponed until next month.",
        "options": ["have been", "is being", "was being", "has been"],
        "answer": 3,
        "explanation": "主语 the annual meeting 为单数，且动作对现在有影响，用现在完成时被动语态。"
    },
    {
        "id": "toeic-p5-628",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "Mr. Tanaka is responsible ______ overseeing the expansion of our overseas branches.",
        "options": ["in", "with", "for", "at"],
        "answer": 2,
        "explanation": "be responsible for 为固定搭配，意为“负责……”。"
    },
    {
        "id": "toeic-p5-629",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "The company has experienced ______ growth in online sales over the past two quarters.",
        "options": ["significantly", "significance", "signify", "significant"],
        "answer": 3,
        "explanation": "修饰名词 growth 需用形容词 significant。"
    },
    {
        "id": "toeic-p5-630",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "Please review the attached document and provide your feedback ______ the end of the week.",
        "options": ["until", "in", "at", "by"],
        "answer": 3,
        "explanation": "by 表示“在……之前（某个时间点）”，常与截止时间连用。"
    },
    {
        "id": "toeic-p5-631",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "We are seeking a candidate ______ has at least five years of project management experience.",
        "options": ["which", "whose", "whom", "who"],
        "answer": 3,
        "explanation": "先行词为人 candidate，且在从句中作主语，用关系代词 who。"
    },
    {
        "id": "toeic-p5-632",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "The administrative assistant organized the files ______ to ensure easy retrieval.",
        "options": ["efficiently", "efficient", "efficiency", "more efficiently"],
        "answer": 0,
        "explanation": "修饰动词 organized 需用副词 efficiently。"
    },
    {
        "id": "toeic-p5-633",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "Delegates attending the symposium are requested to wear ______ identification badges at all times.",
        "options": ["theirs", "them", "themselves", "their"],
        "answer": 3,
        "explanation": "修饰名词 identification badges 需用形容词性物主代词 their。"
    },
    {
        "id": "toeic-p5-634",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "Building maintenance will be conducted this weekend; ______, the office building will be closed on Saturday.",
        "options": ["however", "furthermore", "otherwise", "therefore"],
        "answer": 3,
        "explanation": "前后句为因果关系，前面是原因，后面是结果，用 therefore。"
    },
    {
        "id": "toeic-p5-635",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "Registration for the leadership seminar is open to ______ employees interested in career advancement.",
        "options": ["every", "much", "another", "all"],
        "answer": 3,
        "explanation": "employees 为可数名词复数，all 可修饰复数名词表“所有”。"
    },
    {
        "id": "toeic-p5-636",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "The consulting firm submitted its preliminary findings ______ the executive committee yesterday.",
        "options": ["for", "with", "at", "to"],
        "answer": 3,
        "explanation": "submit sth. to sb. 为固定搭配，意为“向某人提交某物”。"
    },
    {
        "id": "toeic-p5-637",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "Ms. Lopez spoke ______ during the conference call about the new budget allocation.",
        "options": ["persuasively", "persuade", "persuasive", "persuasion"],
        "answer": 0,
        "explanation": "修饰动词 spoke 需用副词 persuasively。"
    },
    {
        "id": "toeic-p5-638",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "Factory workers must wear safety goggles ______ the machinery is operating.",
        "options": ["wherever", "however", "whatever", "whenever"],
        "answer": 3,
        "explanation": "引导时间状语从句意为“无论何时，每当”，应用 whenever。"
    },
    {
        "id": "toeic-p5-639",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "The manager praised the team for their ______ efforts in completing the project ahead of schedule.",
        "options": ["dedicated", "dedicate", "dedication", "dedicating"],
        "answer": 0,
        "explanation": "修饰名词 efforts 需用形容词 dedicated（尽职的、奉献的）。"
    },
    {
        "id": "toeic-p5-640",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "Clients can access their account details securely ______ logging into our online portal.",
        "options": ["throughout", "without", "beside", "by"],
        "answer": 3,
        "explanation": "by doing sth. 表示“通过……方式”，符合语境。"
    },
    {
        "id": "toeic-p5-641",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "The updated software license agreement will take ______ on the first of next month.",
        "options": ["affect", "effective", "effectively", "effect"],
        "answer": 3,
        "explanation": "take effect 为固定搭配，意为“生效”。"
    },
    {
        "id": "toeic-p5-642",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "Mr. Evans decided to postpone his business trip ______ adverse weather conditions.",
        "options": ["even though", "in order that", "as if", "because of"],
        "answer": 3,
        "explanation": "because of 后接名词短语表原因，意为“因为”。"
    },
    {
        "id": "toeic-p5-643",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "The human resources department announced that ______ new employee must complete orientation.",
        "options": ["all", "many", "several", "each"],
        "answer": 3,
        "explanation": "new employee 为单数可数名词，each 可修饰单数名词表“每个”。"
    },
    {
        "id": "toeic-p5-644",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "Please ensure that all office equipment is turned off ______ leaving the building.",
        "options": ["until", "since", "while", "before"],
        "answer": 3,
        "explanation": "表时间先后，离开大楼前关闭设备，用 before。"
    },
    {
        "id": "toeic-p5-645",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "The marketing campaign generated an ______ number of inquiries from potential clients.",
        "options": ["unprecedentedly", "unprecedentedness", "unprecedent", "unprecedented"],
        "answer": 3,
        "explanation": "修饰名词 number 需用形容词 unprecedented（空前的）。"
    },
    {
        "id": "toeic-p5-646",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "To improve customer satisfaction, the store manager handles all complaints ______.",
        "options": ["prompt", "prompts", "promptly", "promptness"],
        "answer": 2,
        "explanation": "修饰动词 handles 需用副词 promptly。"
    },
    {
        "id": "toeic-p5-647",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "The company’s chief executive officer will speak at the international trade conference ______.",
        "options": ["tomorrow", "yesterday", "last week", "ago"],
        "answer": 0,
        "explanation": "will speak 为将来时，时间状语用 tomorrow。"
    },
    {
        "id": "toeic-p5-648",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "Ms. Chen was promoted to senior accountant ______ her exceptional performance and leadership.",
        "options": ["in addition to", "in recognition of", "in spite of", "in case of"],
        "answer": 1,
        "explanation": "in recognition of 意为“表彰，鉴于”，符合晋升原因的语境。"
    },
    {
        "id": "toeic-p5-649",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "The research team presented ______ findings at the annual science and technology symposium.",
        "options": ["they", "them", "their", "theirs"],
        "answer": 2,
        "explanation": "修饰名词 findings 需用形容词性物主代词 their。"
    },
    {
        "id": "toeic-p5-650",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "Interested applicants should submit their resumes ______ email no later than Friday.",
        "options": ["by", "on", "in", "at"],
        "answer": 0,
        "explanation": "by email 为固定搭配，意为“通过电子邮件”。"
    },
    {
        "id": "toeic-p5-651",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "The venue for the annual gala dinner has been changed to a ______ spacious location.",
        "options": ["much", "many", "more", "most"],
        "answer": 2,
        "explanation": "修饰比较级 spacious 需用 more，表示“更大一些”。"
    },
    {
        "id": "toeic-p5-652",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "All visitors must sign in at the security desk ______ entering the manufacturing facility.",
        "options": ["upon", "during", "while", "unless"],
        "answer": 0,
        "explanation": "upon 相当于 as soon as 或 on doing，意为“一……就……”。"
    },
    {
        "id": "toeic-p5-653",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "The maintenance crew inspected the ventilation system ______ to prevent unexpected failures.",
        "options": ["thorough", "thoroughly", "thoroughness", "more thorough"],
        "answer": 1,
        "explanation": "修饰动词 inspected 需用副词 thoroughly。"
    },
    {
        "id": "toeic-p5-654",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "Mr. Patel expects that the new office building ______ completed by the end of next year.",
        "options": ["will be", "has been", "is being", "was"],
        "answer": 0,
        "explanation": "由 by the end of next year 可知用将来时被动语态 will be completed。"
    },
    {
        "id": "toeic-p5-655",
        "exam": "toeic",
        "section": "reading",
        "part": 5,
        "question": "The chief financial officer advised the board to invest ______ in renewable energy sectors.",
        "options": ["wise", "wisely", "wisdom", "wiser"],
        "answer": 1,
        "explanation": "修饰动词 invest 需用副词 wisely。"
    }
]

print(f"Total questions: {len(questions)}")
answers = [q["answer"] for q in questions]
dist = {i: answers.count(i) for i in range(4)}
print("Answer distribution:", dist)

assert len(questions) == 39, f"Expected 39 questions, got {len(questions)}"
ids = [q["id"] for q in questions]
expected_ids = [f"toeic-p5-{i}" for i in range(617, 656)]
assert ids == expected_ids, "IDs do not match expected continuous range"

for q in questions:
    assert len(q["options"]) == 4, f"Question {q['id']} does not have 4 options"
    assert 0 <= q["answer"] <= 3, f"Question {q['id']} answer index out of range"

os.makedirs(r"D:\work\Hermes\testprep-app\data_gen\output", exist_ok=True)
output_path = r"D:\work\Hermes\testprep-app\data_gen\output\toeic-p5_05.json"

with open(output_path, "w", encoding="utf-8") as f:
    json.dump({"questions": questions}, f, ensure_ascii=False, indent=2)

print(f"Successfully generated and validated TOEIC Part 5 questions at {output_path}")
