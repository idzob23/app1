#your task for this exercise is to extend the program you created in Exercise 1 by displaying a message
# to the user when they enter 0 for the "total value".

try:
    total = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    print("That is " + str(round(value*100/total,2)) + "%")
except ValueError:
    print("You need to enter the number. Run the program again")
except ZeroDivisionError:
    print("Your total value cannot be zero")
