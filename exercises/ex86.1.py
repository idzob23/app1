# The user runs the program. The program asks the user to enter "head" or "tail".
# The user flips a coin on their desk, table, floor, etc., and then enters "head" or "tail".
# The user does the same over and over again.
# In each cycle, the program should return the current percentage of heads in the program,
# similar to what you see in the screenshot above.
# Also, you should write each user entry (i.e., head or tail) in a text file using a with-context manager, one entry per line.
#   Throw the coin and enter head or tail here: ? tail
#   Heads: 0.0%
#   Throw the coin and enter head or tail here: ? head
#   Heads: 50.0%
#   Throw the coin and enter head or tail here: ? head
#   Heads: 66.666666666%

# #open empty file
with open("../files/sides.txt", 'w') as file:
    print("")
#
while True:
    with open("../files/sides.txt", 'r') as file:
        sides = file.readlines()

    side = input("Throw the coin and enter head or tail here: ?") + "\n"
    if side not in ['head\n','tail\n']:
        break
    else:
        sides.append(side)

        with open("../files/sides.txt", 'w') as file:
            file.writelines(sides)

        nr_heads = sides.count("head\n")
        percentage = nr_heads / len(sides) * 100

        print(f"Heads: {percentage}%")