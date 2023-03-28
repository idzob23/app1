# Check for strong password that satisfied 3 conditions
# eight characters or longer
# contain at least one digit
# contain at least one uppercase letter




# while True:
#     user_input = input("Enter new password: ")
#     if len(user_input) >= 8 and any(i.isdigit() for i in user_input) and any(i.isupper() for i in user_input):
#         print("Strong password")
#         break
#     else:
#         print("Weak password")



#You can also put True/False in list as answer to all 3 questions
#and then if list have 3 items then the password is strong
result=[]

user_input = input("Enter new password: ")
if len(user_input) >= 8:
    result.append(True)

    for i in user_input:
        if i.isdigit():
            result.append(True)
            break


    for i in user_input:
        if i.isupper():
            result.append(True)
            break


if len(result) == 3:
    print("Strong password")
else:
    print("Weak password")

#second way to test
# result1=[True, True, True]
# print(all(result1))    => True
# result2=[True, False, True]
# print(all(result2))    => False

#This is the case ideal for dictionaries
#because we want to know what is the questions for each answer
#Example
#{'Length':True, 'Digit':True, 'Uppercase':True}



