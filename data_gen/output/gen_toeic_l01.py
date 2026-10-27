import json

questions = [
{
"id":"toeic-l-054",
"exam":"toeic","section":"listening","part":2,
"audio":"Manager: Could you move our meeting to next Tuesday morning? My schedule is completely full this week, and I have several client calls that I cannot postpone. Assistant: I checked the conference room calendar, and Room 302 is free at ten a.m. on Tuesday. Manager: Great. Please invite all the department heads and update the agenda with the new sales figures. Assistant: Done. I have added the agenda to the shared drive and sent invitations to everyone on the list. Manager: Thanks, that saves me a lot of time. Could you also print a copy of the quarterly results for the meeting? Assistant: Of course. I will prepare the handouts and place them in the room before the meeting starts.",
"question":"What does the manager want the assistant to do?",
"options":["Reschedule the meeting","Book a room for Friday","Cancel the meeting","Move the agenda to Room 302"],
"answer":0,
"explanation":"Manager 明确表示把会议挪到下周二上午（move our meeting to next Tuesday），答案为 Reschedule the meeting。"
},
{
"id":"toeic-l-055",
"exam":"toeic","section":"listening","part":2,
"audio":"Employee: I need to book a round-trip flight to Boston for the regional conference next month, and I prefer a direct route if possible. Travel Agent: The cheapest fare leaves early Monday morning and returns Thursday night. Employee: I would rather have an afternoon departure because I have a meeting that morning. Travel Agent: There is one at two thirty p.m. for about fifty dollars more, and it arrives the same evening. Employee: That works for me. Please go ahead and book that flight. Travel Agent: Your confirmation will be emailed to you shortly, and you can check in online twenty-four hours before departure.",
"question":"What does the employee want?",
"options":["A cheaper flight","An evening return","A direct flight only","A later departure time"],
"answer":3,
"explanation":"Employee 说宁愿下午出发（rather have an afternoon departure），因为上午有会议，故选择较晚的起飞时间。"
},
{
"id":"toeic-l-056",
"exam":"toeic","section":"listening","part":2,
"audio":"Buyer: We ordered five hundred printers last month, but only three hundred arrived at our warehouse. Supplier: I apologize for the shortage. We can deliver the remaining two hundred units tomorrow morning. Buyer: That is too late; we need them today because our department is installing the new office system. Supplier: How about half now and half tomorrow afternoon? Our truck is already in your city today. Buyer: Fine, just make sure the first batch arrives before noon, and send me a tracking number. Supplier: Absolutely. I will call you as soon as the driver confirms the delivery time.",
"question":"What solution does the buyer finally accept?",
"options":["Full delivery today","Cancel the order","Split delivery","Return all printers"],
"answer":2,
"explanation":"Buyer 同意了供应商分批送货的建议（half now and half tomorrow afternoon），故答案为 Split delivery。"
},
{
"id":"toeic-l-057",
"exam":"toeic","section":"listening","part":2,
"audio":"Customer: The coffee machine I bought last week stopped working this morning, and it makes a strange noise now. Support Agent: I am sorry to hear that. May I have your order number so I can look it up in our system? Customer: Sure, it is B eight nine four two. I purchased it during the summer sale. Support Agent: Since it is still under warranty, we will send you a replacement at no cost, and you can keep the old unit. Customer: Wonderful, when can I expect it? I use the machine every day at work. Support Agent: Within three to five business days. You will receive a confirmation email with the tracking number today.",
"question":"What will the support agent provide?",
"options":["A full refund","A free replacement","A repair service","A discount voucher"],
"answer":1,
"explanation":"Agent 说机器仍在保修期内，将免费寄送 replacement（replacement at no cost），故选 A free replacement。"
},
{
"id":"toeic-l-058",
"exam":"toeic","section":"listening","part":2,
"audio":"Director: The marketing budget looks overspent for this quarter, and I want to understand why before we plan the next one. Analyst: I reviewed the numbers. Most of it went on the social media campaign for the new product launch. Director: Did that campaign actually increase our sales, or was it a waste of money? Analyst: Yes, revenue from online channels rose by fifteen percent, so the campaign performed well overall. Director: Then let us keep the plan but cut the print advertising costs, and shift those funds to email marketing. Analyst: I will adjust the budget sheet and send it to you by noon with a summary of the changes.",
"question":"What does the director decide?",
"options":["Cut the social media campaign","Increase print advertising","Stop all marketing spending","Keep online but cut print"],
"answer":3,
"explanation":"Director 说线上渠道增收 15%，所以决定继续线上投入同时削减印刷广告（keep the plan but cut print ads）。"
},
{
"id":"toeic-l-059",
"exam":"toeic","section":"listening","part":2,
"audio":"HR Manager: Thank you for coming in today. Do you have any questions about the job or the company culture? Please feel free to ask about anything at all. Candidate: Yes, how many vacation days does the position offer in the first year? HR Manager: Full-time staff receive twenty days per year, plus paid holidays and sick leave. Candidate: That meets my needs. Are the days flexible, or must I take them in fixed blocks? HR Manager: They are flexible, but you should request them two weeks in advance through the online system. Candidate: Thank you for your time. I look forward to hearing from you next week.",
"question":"What is the candidate most concerned about?",
"options":["Vacation allowance","Salary level","Job location","Start date"],
"answer":0,
"explanation":"Candidate 问的是年假天数（how many vacation days），HR 答二十天，所以最关心的是假期津贴。"
},
{
"id":"toeic-l-060",
"exam":"toeic","section":"listening","part":2,
"audio":"Supervisor: We are running low on office supplies. Could you order some paper and toner for the printers? We need enough for the whole month. Staff: I will place the order online this afternoon from our approved supplier. Supervisor: Please choose the fastest shipping option so the items arrive before the audit next week. Staff: There is overnight delivery for an extra ten dollars, or standard shipping in three days. Supervisor: That is acceptable. Just keep the receipt for reimbursement and send me a copy. Staff: Understood. I will forward the invoice to you as soon as the order is confirmed.",
"question":"What does the supervisor want?",
"options":["The cheapest option","Delivery to home","Faster shipping","A printed catalog"],
"answer":2,
"explanation":"Supervisor 明确要求最快的运输方式（fastest shipping option），故答案为 Faster shipping。"
},
{
"id":"toeic-l-061",
"exam":"toeic","section":"listening","part":2,
"audio":"Coordinator: The video conference keeps disconnecting during the presentation, and the audio cuts out every few minutes. Tech Support: Please check your internet connection and the signal strength near your desk. Coordinator: I restarted the router, but the connection is still slow in the meeting room. Tech Support: Try using an ethernet cable instead of Wi-Fi, since the walls may block the wireless signal. Coordinator: Let me try that now. It looks stable, and the presentation resumed without any delay. Tech Support: Good. You can proceed with the meeting, and feel free to call us again if the issue returns.",
"question":"What does tech support recommend?",
"options":["Restart the laptop","Use a wired connection","Upgrade the software","Cancel the meeting"],
"answer":1,
"explanation":"Tech Support 建议使用网线而不是 Wi-Fi（ethernet cable instead of Wi-Fi），即使用有线连接。"
},
{
"id":"toeic-l-062",
"exam":"toeic","section":"listening","part":2,
"audio":"Employee: I submitted my travel expense report last week, including all the receipts and the hotel bill. I thought everything was in order. Finance Officer: I have not received it yet. Did you email it to the wrong person by mistake? Employee: No, I attached it to your email address, the one ending in company dot com. Finance Officer: Hmm, let me check the spam folder. Actually, I found it. Please fill out the new reimbursement form instead. Employee: I will do it right away. Should I resubmit the receipts as well? Finance Officer: Yes, attach them again, and use this week's version of the form, not the old one.",
"question":"What does the finance officer ask the employee to do?",
"options":["Email the report again","Delete the old report","Visit the finance office","Complete a new form"],
"answer":3,
"explanation":"Finance Officer 找到报告后要求改用新的报销表格（fill out the new reimbursement form），故选 D。"
},
{
"id":"toeic-l-063",
"exam":"toeic","section":"listening","part":2,
"audio":"Manager: We have an important client visiting tomorrow morning, so we need the contract drafts ready tonight. Everything must look professional. Intern: Should I print the contract drafts for the meeting, or will they use tablets? I can also prepare digital copies. Manager: Yes, please print them, but double-check the figures in the pricing section first. Intern: I noticed a discrepancy in the appendix; the total does not match the itemized costs. Manager: Fix it before the client arrives. The client values accuracy over speed, so take your time. Intern: Understood. I will correct it tonight and send you the final version for approval.",
"question":"What does the manager emphasize?",
"options":["Accurate data","Printing speed","Client availability","Contract length"],
"answer":0,
"explanation":"Manager 说客户重视准确性胜过速度（values accuracy over speed），所以强调准确数据。"
},
{
"id":"toeic-l-064",
"exam":"toeic","section":"listening","part":2,
"audio":"Sales: Our big order for office furniture is delayed at the port, and the client is getting nervous. Logistics: We received a notification from the shipping company. The container will arrive on Friday instead of Wednesday. Sales: The client is expecting delivery by Wednesday, so Friday is simply not acceptable to them. Logistics: I can arrange for expedited truck delivery once the container clears customs, likely Thursday evening. Sales: Please do that; we cannot disappoint the client, since this is a major account for us. Logistics: I will contact the trucking company now and update you as soon as the schedule is confirmed.",
"question":"What will logistics arrange?",
"options":["A refund for the client","A smaller shipment","Expedited truck delivery","A meeting with customs"],
"answer":2,
"explanation":"Logistics 说在清关后安排加急卡车运输（expedited truck delivery），以赶上客户预期。"
},
{
"id":"toeic-l-065",
"exam":"toeic","section":"listening","part":2,
"audio":"HR: The safety training session is optional this year, so you are not required to attend. Participation is completely up to each employee. Employee: Should I still attend it? I want to make sure I do not miss anything important. HR: Definitely. Many new hires found it very helpful, and it covers the updated fire procedures. Employee: I will register by the end of the week. Does the session include a practical drill? HR: Yes, there is a short drill, and do not forget to collect the attendance certificate afterward. Employee: Great, I need that certificate for my professional development file, so I will be there.",
"question":"What does HR recommend?",
"options":["Skip the training","Attend the training","Get a different certificate","Register only online"],
"answer":1,
"explanation":"HR 用 Definitely 强烈建议参加，员工确认会注册（register by the end of the week），故答案为 Attend the training。"
},
{
"id":"toeic-l-066",
"exam":"toeic","section":"listening","part":2,
"audio":"Director: We are changing the remote work policy next month, so please pay attention to the new rules. The change takes effect on the first of the month. Staff: Will we still be able to work from home three days a week as we do now? Director: No, the new policy allows two days from home and three days in the office each week. Staff: I have a longer commute now, so that schedule will be difficult for me. Director: You may work from home four days if your manager approves it, with one office day required. Staff: That still gives me enough office time. Thank you, and I will speak to my manager this week.",
"question":"What exception is allowed?",
"options":["Work remotely full time","No remote work at all","Five days in the office","Remote work four days a week"],
"answer":3,
"explanation":"Director 说如果经理批准可以每周在家工作四天（work from home four days if your manager approves），故选 D。"
},
{
"id":"toeic-l-067",
"exam":"toeic","section":"listening","part":2,
"audio":"Project Manager: The office renovation is ahead of schedule, which is great news for the whole team. The contractors have been very reliable so far. Admin: Do you think it will be finished before the holiday break at the end of the month? Project Manager: Yes, the painters finish on Thursday, and the new lighting will be installed on Friday. Admin: And the carpet installers? Have they confirmed their dates yet? Project Manager: They start next Monday and finish before Friday, so the rooms will be ready in time. Admin: Excellent. I will book the cleaning service for Saturday so the office is spotless by Monday.",
"question":"What does the project manager say about the timeline?",
"options":["It is ahead of schedule","It is behind schedule","It is on time","It is finished already"],
"answer":0,
"explanation":"Project Manager 第一句就说装修领先于计划（ahead of schedule），所以答案是 A。"
},
{
"id":"toeic-l-068",
"exam":"toeic","section":"listening","part":2,
"audio":"Account Manager: I need to leave a message for Ms. Chen about the client presentation tomorrow. It is an important meeting for the new contract. Receptionist: She is in a meeting until two o'clock, but I can take a message for you. Account Manager: Please tell her the presentation slides are ready and the room is confirmed. Receptionist: Would you like me to email them to her directly so she can review them before the meeting? Account Manager: Yes, that would be faster. Please also ask her to check the pricing section. She can call me if she has any comments. Receptionist: No problem. I will send them right now and copy the sales director as well.",
"question":"What will the account manager do?",
"options":["Wait for Ms. Chen","Postpone the meeting","Email the slides","Call Ms. Chen again"],
"answer":2,
"explanation":"Account Manager 同意前台直接发送邮件（Yes, that would be faster），所以选择 Email the slides。"
},
{
"id":"toeic-l-069",
"exam":"toeic","section":"listening","part":2,
"audio":"Procurement: The vendor wants to renew the contract for another year, and they sent the updated terms to my office this morning. Legal: I reviewed the terms carefully. There is an unfair liability clause that puts all the risk on us, and we cannot accept that. Procurement: Can we negotiate better terms before we sign anything, or is the document final? Legal: Yes, we can ask for a cap on damages and a shorter termination notice period as well. Procurement: I will contact them this afternoon to discuss our concerns and request the changes. Legal: Let me know if they refuse, and I will prepare an alternative contract with another supplier.",
"question":"What is Legal's main concern?",
"options":["Contract price","A liability clause","Payment method","Delivery schedule"],
"answer":1,
"explanation":"Legal 指出条款中有不公平的责任条款（unfair liability clause），这是主要担忧。"
},
{
"id":"toeic-l-070",
"exam":"toeic","section":"listening","part":2,
"audio":"Manager: When will the quarterly report be ready? The board is asking for an update. They need the figures for the meeting. Accountant: I am finalizing the numbers now, and I expect to finish by three o'clock this afternoon. Manager: Could you send it to the board before five so they can review it tonight? Accountant: That should be fine, but the analysis section is not complete yet. Manager: Then send what you have and add the analysis tomorrow, when it is ready. Accountant: I will mark it as draft so the board knows the analysis is still coming, and email it before five.",
"question":"What does the accountant plan to send?",
"options":["Nothing until complete","Only the analysis","A verbal summary","The numbers first"],
"answer":3,
"explanation":"Accountant 被要求先发送现有内容，明天再加分析（send what you have and add the analysis tomorrow），所以先发数据。"
},
{
"id":"toeic-l-071",
"exam":"toeic","section":"listening","part":2,
"audio":"Employee: I would like to reserve a table for six this evening, preferably with a nice view. We are celebrating a colleague's promotion. Restaurant: We have a booth available at seven o'clock, right by the window. Employee: Is there a view of the garden? My guests enjoy scenery with dinner. Restaurant: The garden tables are only available outside, and the weather is quite cold tonight. Employee: It is a bit chilly, so we would rather stay indoors if possible. Please make sure we have enough space for six. Restaurant: We can move you to the indoor area near the window, and I will confirm the reservation for seven.",
"question":"Why does the employee decline the booth?",
"options":["It has no garden view","It is too small","It is fully booked","The price is too high"],
"answer":0,
"explanation":"Employee 询问花园景观，但花园桌只能户外（only available outside），今晚较冷所以不选，故为没有花园景观。"
},
{
"id":"toeic-l-072",
"exam":"toeic","section":"listening","part":2,
"audio":"Supervisor: Do you prefer a hybrid schedule or full remote work for the coming months? Employee: Full remote would suit me better, since I live quite far from the office. The commute takes almost two hours each way. Supervisor: That is allowed for your role, and many team members work remotely now. Will you need any equipment? Employee: Yes, I need a second monitor and a better headset for my video calls. Supervisor: I will submit the request to IT today, and you should receive everything by next week. Employee: Thank you very much. I appreciate the support, and I will start setting up my home office.",
"question":"What does the supervisor agree to?",
"options":["Hybrid schedule","Extra equipment only","Full remote work","No change"],
"answer":2,
"explanation":"Supervisor 说该职位允许全职远程工作（That is allowed for your role），故选 C。"
},
{
"id":"toeic-l-073",
"exam":"toeic","section":"listening","part":2,
"audio":"Accounts Payable: Your invoice for office supplies is ready for payment, and everything looks correct in the system. The department approved the amount last week. Purchaser: When will the funds be transferred to the vendor's account? They are asking for an update. Accounts Payable: Typically within thirty days, according to our standard payment policy, unless we agree otherwise. Purchaser: Our vendor asks for fifteen days, and they mentioned this condition in the signed contract. Accounts Payable: I will confirm the payment terms with them today and see if we can move the date up. Purchaser: Please let me know the result, since the vendor is waiting for a confirmation from us.",
"question":"What will accounts payable do next?",
"options":["Reject the invoice","Contact the vendor","Cancel the order","Delay payment by thirty days"],
"answer":1,
"explanation":"Accounts Payable 说今天会与供应商确认付款条款（confirm the payment terms with them today），故选 B。"
},
{
"id":"toeic-l-074",
"exam":"toeic","section":"listening","part":2,
"audio":"HR Coordinator: We are planning a team building event, and we want everyone's input on the date and the activities. Staff: Is it on Friday afternoon or during the weekend? Saturday works better for me. What activities are you considering? HR Coordinator: We thought about Saturday morning, since the office is closed and the venue is free that day. We have indoor and outdoor options, including games, a workshop, and a barbecue lunch. Staff: Indoor is safer given the forecast, because rain is expected for the whole weekend, so let us book the indoor venue. HR Coordinator: Then it is indoor on Saturday, and I will send you the schedule and directions by email.",
"question":"Why did the staff choose the indoor event?",
"options":["It is cheaper","More participants","A longer duration","The weather forecast"],
"answer":3,
"explanation":"Staff 说室内更安全（safer given the forecast），因为预报周末有雨，故选 D。"
},
{
"id":"toeic-l-075",
"exam":"toeic","section":"listening","part":2,
"audio":"Manager: Keep those files confidential until the merger is announced to the public next month, and do not share them with anyone. Security is our top priority this quarter. Employee: Should I email them to the legal team for their review, or keep them offline? Manager: Do not email them. Use the secure server instead, and set a password on the folder. Employee: I will upload them right away and make sure only the legal team has access. Manager: And please delete the copies on your laptop so nothing is left on your device. Employee: Understood. I will do that immediately, and then send you a confirmation message.",
"question":"What does the manager tell the employee to do?",
"options":["Use the secure server","Email the files","Delete all files","Announce the merger"],
"answer":0,
"explanation":"Manager 明确说不要发邮件，改用安全服务器（use the secure server instead），故选 A。"
}
]

with open('D:/work/Hermes/testprep-app/data_gen/output/toeic-l_01.json', 'w', encoding='utf-8') as f:
    json.dump({"questions": questions}, f, ensure_ascii=False, indent=2)

print(f"Wrote {len(questions)} questions")
