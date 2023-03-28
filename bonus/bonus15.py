"""
Ask user 2 questions and after that present user's score like this:
1 Correct Answer: User Answer: 3, Correct Answer: 3
2 Incorrect Answer: User Answer: 2, Correct Answer: 1
Score 1/2
"""
import json
score = 0
message=[]


with open("files/bonus15.json", "r") as file:
    content = file.read()       #result is string

data = json.loads(content)      #result is list

for question in data:
    print(question['question_text'])
    for index, alternative in enumerate(question["alternatives"]):
        print(f"{index+1}-{alternative}")

    user_answer = int(input("Enter your answer: "))
    question['user_answer'] = user_answer
    if question['user_answer'] == question['correct_answer']:
        score += 1
        message.append(f"Correct Answer: User Answer: {question['user_answer']}, Correct Answer: {question['correct_answer']}")
    else:
        message.append(f"Incorrect Answer: User Answer: {question['user_answer']}, Correct Answer: {question['correct_answer']}")


for index, line in enumerate(message):
    print(f"{index+1} {line}")
print(f"Score {score}/{len(data)}")


#2nd way

#   user_answer = int(input("Enter your answer: "))
#     correct_answer = question['correct_answer']
#     if user_answer == correct_answer:
#         score += 1
#         message.append(f"Correct Answer: User Answer: {user_answer}, Correct Answer: {correct_answer}")
#     else:
#         message.append(f"Incorrect Answer: User Answer: {user_answer}, Correct Answer: {correct_answer}")
#
#
# for index, line in enumerate(message):
#     print(f"{index+1} {line}")
# print(f"Score {score}/{len(data)}")