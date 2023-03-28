#ask user 3 questions: today's date, rate your mood today and enter some thoughts
#create txt file with name of answer from 1st question and put second and third answer as file content

user_date = input("Enter today's date: ")
user_mood = input("Rate your moood today from 1 to 10: ")
user_content = input("Let your thoughts flow: ")

with open(f"../journal/{user_date}.txt", 'w') as file:
    file.write(user_mood + 2*'\n')
    file.write(user_content)