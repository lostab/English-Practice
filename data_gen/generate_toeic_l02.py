import json

questions = [
    {
        "id": "toeic-l-076",
        "exam": "toeic",
        "section": "listening",
        "part": 2,
        "audio": "Manager: We need to finalize the budget for the new product launch by Friday. Finance: I am reviewing the projected costs now, but I have not finished the spreadsheet yet. Manager: Make sure to include the marketing expenses as well. Finance: I have not added the advertising budget to the spreadsheet so far. Manager: Please add it and send me the complete report tonight. Finance: I will finish it before I leave the office at six. Manager: Great, thank you for your quick response.",
        "question": "What does the manager ask the finance team to do?",
        "options": [
            "Exclude the advertising costs",
            "Include the marketing budget",
            "Postpone the report to Monday",
            "Cancel the product launch"
        ],
        "answer": 1,
        "explanation": "Manager 要求把广告预算一并计入（include the marketing expenses），故选 Include the marketing budget。"
    },
    {
        "id": "toeic-l-077",
        "exam": "toeic",
        "section": "listening",
        "part": 2,
        "audio": "Client: Our servers have been down for two hours this morning, and we cannot access any files. IT Support: I checked the system logs, and there was an unexpected security breach last night. Client: Can you restore all the data from the backup we made? IT Support: Yes, we have a complete backup from midnight that should cover everything. Client: Please prioritize the sales database, since we have orders pending. IT Support: It is already being restored right now, and I will monitor the process closely. Client: Is there any chance the data might be corrupted during restoration? IT Support: The backup was taken from a clean snapshot, so the data should be intact. Client: Thank you, I appreciate your help.",
        "question": "What is the client most concerned about?",
        "options": [
            "Installing new security software",
            "Restoring the sales database",
            "Changing the server passwords",
            "Hiring a security consultant"
        ],
        "answer": 1,
        "explanation": "Client 明确要求优先恢复销售数据库（prioritize the sales database），故选 Restoring the sales database。"
    },
    {
        "id": "toeic-l-078",
        "exam": "toeic",
        "section": "listening",
        "part": 2,
        "audio": "Receptionist: Good morning. Thank you for calling Meridian Office Supplies. How may I direct your call? Buyer: I would like to speak to Mr. Tanaka in the purchasing department. Receptionist: I am afraid he is in a meeting with the suppliers until noon today. Buyer: Then please ask him to call me back as soon as he is free. Receptionist: Certainly, sir. May I take a message for him? Buyer: Yes, tell him to check the latest price list that I sent this morning. Receptionist: I will make sure he gets it today.",
        "question": "What message does the buyer leave?",
        "options": [
            "To postpone the meeting",
            "To send a new price list",
            "To check a sent price list",
            "To order more products"
        ],
        "answer": 2,
        "explanation": "Buyer 请转告 Tanaka 查看他今早发的价格表（check the latest price list that I sent），故选 To check a sent price list。"
    },
    {
        "id": "toeic-l-079",
        "exam": "toeic",
        "section": "listening",
        "part": 2,
        "audio": "Supervisor: The training workshop has been moved to next week because of the room conflict. Trainer: Did the participants get notified about the new date yet? Supervisor: Not yet. I will send out the updated schedule today by email. Trainer: Please let me know if anyone cancels after seeing it. Supervisor: I will collect all the confirmations by tomorrow afternoon. Trainer: Thanks for keeping me in the loop about the changes.",
        "question": "What has the supervisor decided to do?",
        "options": [
            "Cancel the workshop",
            "Send the updated schedule",
            "Reschedule the trainer",
            "Postpone the confirmations"
        ],
        "answer": 1,
        "explanation": "Supervisor 说今天就把更新后的日程发出去（send out the updated schedule today），故选 Send the updated schedule。"
    },
    {
        "id": "toeic-l-080",
        "exam": "toeic",
        "section": "listening",
        "part": 2,
        "audio": "Accountant: I have to tell you that the bank transfer has been delayed by one business day. Purchasing: Is that because of the missing signature on the form? Accountant: Yes, the payment form needs the director's approval before it can go through. Purchasing: I will get it signed this afternoon without any delay. Accountant: Then the payment should clear by Wednesday at the latest. Purchasing: Please let me know as soon as it is done.",
        "question": "Why was the payment delayed?",
        "options": [
            "The bank was closed",
            "The supplier changed",
            "A signature was missing",
            "The amount was wrong"
        ],
        "answer": 2,
        "explanation": "Accountant 说转账需要董事签字批准（needs the director's approval），故选 A signature was missing。"
    },
    {
        "id": "toeic-l-081",
        "exam": "toeic",
        "section": "listening",
        "part": 2,
        "audio": "HR: The annual performance review cycle starts next Monday, so please be prepared. Manager: I will schedule one-on-one sessions with every member of my team. HR: Remember to update the online evaluation forms before the meetings begin. Manager: Actually, I planned to print paper copies for each employee. HR: The online system works much better for tracking the progress. Manager: You are right. I will use the digital forms instead of the printed ones.",
        "question": "How will the manager conduct the reviews?",
        "options": [
            "With printed paper forms",
            "With the online system",
            "By phone with each person",
            "In a group meeting"
        ],
        "answer": 1,
        "explanation": "Manager 被说服改用线上系统（use the digital forms instead），故选 With the online system。"
    },
    {
        "id": "toeic-l-082",
        "exam": "toeic",
        "section": "listening",
        "part": 2,
        "audio": "Travel Agent: I should mention that the train fare has increased by fifteen percent this month. Traveler: That is higher than I expected to pay for the trip. Travel Agent: You can still save money by booking a round-trip ticket instead. Traveler: I usually only need a one-way trip for this kind of visit. Travel Agent: The round-trip discount is quite attractive, though. Traveler: Okay, let me think about it, and I will book online tonight.",
        "question": "What is the traveler planning to do?",
        "options": [
            "Buy a round-trip ticket",
            "Book a one-way trip",
            "Cancel the entire trip",
            "Take a different train"
        ],
        "answer": 1,
        "explanation": "Traveler 说通常只需要单程票（only need a one-way trip），并打意今晚线上订票，故选 Book a one-way trip。"
    },
    {
        "id": "toeic-l-083",
        "exam": "toeic",
        "section": "listening",
        "part": 2,
        "audio": "Customer: I ordered a new laptop from your website, but it arrived without a charger. Support Agent: I am sorry about that, and I apologize for the inconvenience. Let me check your order details. Customer: It was delivered two days ago to my office address. Support Agent: I found the order, and we will ship a replacement charger today. Customer: Will it arrive by tomorrow morning? Support Agent: Yes, it is going out with expedited shipping at no cost to you.",
        "question": "What will the support agent send?",
        "options": [
            "A new laptop entirely",
            "A replacement charger",
            "A refund for the order",
            "A discount coupon"
        ],
        "answer": 1,
        "explanation": "Support Agent 确认今天寄出替换充电器（ship a replacement charger today），故选 A replacement charger。"
    },
    {
        "id": "toeic-l-084",
        "exam": "toeic",
        "section": "listening",
        "part": 2,
        "audio": "Project Lead: The design mockups are due by tomorrow noon, so we are on a tight schedule. Designer: Do not worry. I have finished the main screens for the desktop version already. Project Lead: Have you included the mobile version in the set of mockups? Designer: Not yet, but I am working on it right now at my desk. Project Lead: Please finish it before the team review starts in the afternoon. Designer: I will send it to you by five o'clock today.",
        "question": "What is the designer still working on?",
        "options": [
            "The mobile version",
            "The main screens",
            "The team review",
            "The project budget"
        ],
        "answer": 0,
        "explanation": "Designer 说移动版本还没完成（working on it right now），故选 The mobile version。"
    },
    {
        "id": "toeic-l-085",
        "exam": "toeic",
        "section": "listening",
        "part": 2,
        "audio": "Executive: The quarterly earnings call is scheduled for next Friday morning at ten. CFO: Will the board members attend in person or join remotely this time? Executive: Most of them will join by video conference from their offices. CFO: I have to admit that the presentation deck is not ready yet. Executive: Then finish it by tomorrow morning without any further delay. CFO: Understood. I will circulate it for review afterward.",
        "question": "What does the executive want the CFO to do?",
        "options": [
            "Cancel the earnings call",
            "Complete the presentation deck",
            "Attend by video conference",
            "Skip the board meeting"
        ],
        "answer": 1,
        "explanation": "Executive 要求 CFO 明早前完成演示文稿（finish it by tomorrow morning），故选 Complete the presentation deck。"
    },
    {
        "id": "toeic-l-086",
        "exam": "toeic",
        "section": "listening",
        "part": 2,
        "audio": "Supplier: I am afraid the raw material shipment will be late again this month. Purchasing: How late exactly will it be arriving at our warehouse? Supplier: The customs inspection has added about three days to the schedule. Purchasing: We cannot delay production by that long, so we need a solution. Supplier: We can ship half of the order now and the rest next week. Purchasing: Send half now, and we will manage the shortfall for the time being.",
        "question": "What does purchasing accept from the supplier?",
        "options": [
            "A full delay",
            "A partial shipment",
            "A lower price",
            "A refund quickly"
        ],
        "answer": 1,
        "explanation": "Purchasing 同意先收一半货（Send half now），接受分批出货，故选 A partial shipment。"
    },
    {
        "id": "toeic-l-087",
        "exam": "toeic",
        "section": "listening",
        "part": 2,
        "audio": "IT: Your computer needs a security update before you can connect to the network. User: Can I skip the update now and install it later in the week? IT: No, the firewall blocks any systems that have not been patched yet. User: Okay, then I will install it right away at my workstation. IT: The update will take about ten minutes, so please do not turn it off. User: I have time before my meeting, so please guide me through the process.",
        "question": "What does IT require the user to do?",
        "options": [
            "Upgrade the hardware",
            "Install a security update",
            "Contact the help desk",
            "Change the password"
        ],
        "answer": 1,
        "explanation": "IT 要求先安装安全更新才能联网（needs a security update），故选 Install a security update。"
    },
    {
        "id": "toeic-l-088",
        "exam": "toeic",
        "section": "listening",
        "part": 2,
        "audio": "Coordinator: I have some bad news. The venue booking for the conference just got canceled. Organizer: Why did that happen when we confirmed it last month? Coordinator: The hotel renovated our ballroom unexpectedly, so they cannot host us. Organizer: Do we have any alternative location available for the same date? Coordinator: Yes, the convention center is available tomorrow for our event. Organizer: Book it immediately, because we cannot move the event date.",
        "question": "What did the coordinator recommend?",
        "options": [
            "Cancel the event",
            "Postpone to next year",
            "Use the convention center",
            "Move to a smaller room"
        ],
        "answer": 2,
        "explanation": "Coordinator 提出会展中心明后天可用（the convention center is available），故选 Use the convention center。"
    },
    {
        "id": "toeic-l-089",
        "exam": "toeic",
        "section": "listening",
        "part": 2,
        "audio": "Employee: My health insurance plan changes next month, and I need some advice. HR: Did you review the new options that were sent to your email? Employee: Yes, I read them, but I am not sure which plan to pick. HR: The monthly premium is lower with the basic plan for singles. Employee: I want more coverage for my family members, though. HR: Then the premium plan fits your needs better, in my opinion.",
        "question": "Which plan does the employee prefer?",
        "options": [
            "The basic plan",
            "The premium plan",
            "The out-of-pocket plan",
            "No insurance at all"
        ],
        "answer": 1,
        "explanation": "Employee 需要更多家庭保障（more coverage for my family），HR 推荐 premium plan，故选 The premium plan。"
    },
    {
        "id": "toeic-l-090",
        "exam": "toeic",
        "section": "listening",
        "part": 2,
        "audio": "Manager: The client asked for a discount on the bulk order they placed yesterday. Sales: We can offer ten percent off the total, but not more than that. Manager: That is within my limit, so we can accept the request. Sales: Should I confirm the final price with the client right now? Manager: Yes, send them the revised quote by the end of the day. Sales: I will attach the updated contract to the email as well.",
        "question": "What does the manager authorize?",
        "options": [
            "A fifteen percent discount",
            "A ten percent discount",
            "No discount at all",
            "A free trial period"
        ],
        "answer": 1,
        "explanation": "Manager 表示 10% 折扣在权限内（within my limit），同意此幅度，故选 A ten percent discount。"
    },
    {
        "id": "toeic-l-091",
        "exam": "toeic",
        "section": "listening",
        "part": 2,
        "audio": "Recruiter: We have three candidates for the open position in the sales team. Interviewer: Have you screened all of their resumes and application materials? Recruiter: Yes, I have, and two of them have highly relevant experience. Interviewer: I would like to meet all three candidates in person. Recruiter: Their interviews are already set for next Tuesday afternoon. Interviewer: Please add me to the calendar invite for all the sessions. Recruiter: Done. You will receive the confirmation shortly.",
        "question": "What does the interviewer want?",
        "options": [
            "To meet all candidates",
            "To hire directly",
            "To cancel the interviews",
            "To extend the deadline"
        ],
        "answer": 0,
        "explanation": "Interviewer 明确要见全部三位候选人（meet all three candidates），故选 To meet all candidates。"
    },
    {
        "id": "toeic-l-092",
        "exam": "toeic",
        "section": "listening",
        "part": 2,
        "audio": "Assistant: The conference room is booked from two to four this afternoon. Meeting Planner: Can we move our discussion to three because of the schedule change? Assistant: Room 204 has an opening at three, so that should work. Meeting Planner: Please reserve that one instead of the original room. Assistant: Should I send out the revised invitation to all the attendees? Meeting Planner: Yes, notify everyone about the new room number right away.",
        "question": "What did the meeting planner request?",
        "options": [
            "To cancel the meeting",
            "To use a different room",
            "To end the meeting early",
            "To extend the time"
        ],
        "answer": 1,
        "explanation": "Meeting Planner 要求改订 204 号房（reserve that one instead），故选 To use a different room。"
    },
    {
        "id": "toeic-l-093",
        "exam": "toeic",
        "section": "listening",
        "part": 2,
        "audio": "Customer: The software keeps crashing whenever I open large files on my computer. Support: Have you tried closing the application and restarting it completely? Customer: Yes, I have, but the problem still happens every time. Support: In that case, your version of the software may be outdated. Customer: When was the latest update released by your company? Support: We released a fix last week that addresses this exact issue. Customer: I will update it right away and see if that helps.",
        "question": "What does support suggest?",
        "options": [
            "Reinstalling the software",
            "Restarting the computer",
            "Updating to the latest version",
            "Deleting large files"
        ],
        "answer": 2,
        "explanation": "Support 指出软件版本可能过时（version may be outdated），应升级，故选 Updating to the latest version。"
    },
    {
        "id": "toeic-l-094",
        "exam": "toeic",
        "section": "listening",
        "part": 2,
        "audio": "Logistics: The delivery truck broke down on the highway near the city center. Warehouse: Did any of the goods get damaged during the breakdown? Logistics: No, everything is secure in the trailer, so do not worry. Warehouse: When will the shipment actually arrive at our warehouse? Logistics: Another truck is being sent right now to transfer the cargo. Warehouse: Just keep me posted on the estimated time of arrival. Logistics: I will text you as soon as there is any news.",
        "question": "What happens next in the delivery?",
        "options": [
            "The shipment is lost",
            "A replacement truck is sent",
            "The warehouse closes",
            "The customer is refunded"
        ],
        "answer": 1,
        "explanation": "Logistics 说另一辆卡车正被派出转运（Another truck is being sent right now），故选 A replacement truck is sent。"
    },
    {
        "id": "toeic-l-095",
        "exam": "toeic",
        "section": "listening",
        "part": 2,
        "audio": "Analyst: The quarterly sales figures look very promising compared to last year. Director: Did the marketing team run the email campaign we discussed? Analyst: Yes, they did, and the open rates were above the average. Director: What about the social media advertisements this quarter? Analyst: Engagement doubled compared to the previous month, which is great. Director: Excellent. Let us keep the current strategy for now.",
        "question": "What does the director decide?",
        "options": [
            "To change the strategy",
            "To cut the budget",
            "To continue the strategy",
            "To hire more staff"
        ],
        "answer": 2,
        "explanation": "Director 说暂时保持现有策略（keep the current strategy），故选 To continue the strategy。"
    },
    {
        "id": "toeic-l-096",
        "exam": "toeic",
        "section": "listening",
        "part": 2,
        "audio": "Facilities: There is a water leak in the second-floor restroom near the elevators. Maintenance: I am checking the pipes right now to find the source of it. Facilities: Should we close the restroom to the public for safety? Maintenance: Yes, keep it closed until the repair is completely finished. Facilities: I expect to finish the repair within an hour from now. Facilities: Please tell the cleaning crew about it as well.",
        "question": "What will the facilities team do?",
        "options": [
            "Hire a plumber immediately",
            "Shut down the water main",
            "Post a warning sign",
            "Call the manager"
        ],
        "answer": 2,
        "explanation": "Facilities 说会在入口贴告示（put up a sign at the entrance），故选 Post a warning sign。"
    }
]

# Final validation
ids = [q["id"] for q in questions]
expected_ids = [f"toeic-l-{i:03d}" for i in range(76, 97)]
if ids == expected_ids:
    print("✓ IDs are sequential and complete")
else:
    print("✗ ID mismatch:", ids)
    print("Expected:", expected_ids)

for q in questions:
    wc = len(q["audio"].split())
    if not (90 <= wc <= 160):
        print(f"✗ {q["id"]}: {wc} words (expected 90-160)")
    opts = q["options"]
    if len(opts) != 4 or len(set(opts)) != 4:
        print(f"✗ {q["id"]}: options count or uniqueness error")
    if not (0 <= q["answer"] <= 3):
        print(f"✗ {q["id"]}: invalid answer {q["answer"]}")
    if len(q["explanation"]) > 90:
        print(f"✗ {q["id"]}: explanation too long ({len(q["explanation"])} chars)")

print("\nAnswer distribution:", {i: sum(1 for q in questions if q["answer"] == i) for i in range(4)})
print("Done!")
