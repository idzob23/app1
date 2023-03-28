# Create a script that asks the user to enter a password.
# Then create a function that checks the strength of the user password.
# The function should return Strong Password if all of the following conditions are true:
# Eight or more characters
# At least one uppercase letter.
# At least one digit.
user_input = input("Enter new password: ")


def check_length(input_string):
    if len(input_string) >= 8:
        return True


def check_uppercase(input_string):
    for i in input_string:
        if i.isupper():
            return True
    return False


def check_digit(input_string):
    for i in input_string:
        if i.isdigit():
            return True
    return False


result = [check_length(user_input), check_uppercase(user_input), check_digit(user_input)]

if all(result):
    print("Strong password")
else:
    print("Weak password")
