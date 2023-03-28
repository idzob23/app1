#  Your task is to create a program that generates a random whole number.
#  Here is how the program should behave:
# Enter the lower bound: 1
# enter the upper bound: 10
# 7

from random import randint

lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

print(randint(lower, upper))
