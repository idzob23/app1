# Write a program that asks users to enter a password.
# Then, it checks if the password length is greater than 7 and returns "Great password there!".
# If the password has 7 or fewer characters, the program returns, "Your password is weak".


user_input = input("Enter a new password: ")
if len(user_input) > 7:
    print("Great password there!")
else:
    print("Your password is weak")



