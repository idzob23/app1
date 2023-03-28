# Write a program that gets a list of names from the user and returns the number of names given.
# You are encouraged to use a function.




user_names = input("Enter names separate by the commas (no spaces): ")

def items_number(input_string):
    #put input string in list
    item_list = input_string.split(',')
    return len(item_list)

result = items_number(user_names)
print(result)

