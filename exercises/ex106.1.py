#Build a percentage calculator that gets from the user the "total value" and the "value" and returns the percentage:
#The program should also print a message if the user doesn't enter a number for the "total value or for the "value":

try:
    total = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    print("That is " + str(round(value*100/total,2)) + "%")
except ValueError:
    print("You need to enter the number. Run the program again")
