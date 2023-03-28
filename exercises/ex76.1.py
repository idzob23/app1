names = ["john smith", "jay santi", "eva kuki"]

# Extend the code above so the code capitalizes all the names and the surnames of the list and then prints the new list.
# The output of your code should be as below:
# ['John Smith', 'Jay Santi', 'Eva Kuki']

new_names = [item.title() for item in names]
print(new_names)