#Optimising code from main62.py

#You may first  want to delete item without showing or adding
with open('todos.txt', 'r') as file:
    todos = file.readlines()

while True:
    user_action = input("Type add, show, edit, delete or exit: ")
    user_action = user_action.strip()

    if user_action == 'add':
        # 1st optimisation -> with-content-manager, this will always close the file even if we have some problems in code
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        todo = input("Enter a todo: ") + "\n"
        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action in ('show','display'):

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")

    elif user_action == 'edit':
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")
        user_number = int(input("Please, choose number for editing: "))
        while user_number not in range(1, len(todos) + 1):
            print("Wrong number!!!")
            user_number = int(input("Please, choose number for editing: "))
        user_value = input("Enter new value: ") + "\n"
        todos[user_number-1] = user_value
        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action == 'delete':
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")
        user_number = int(input("Please, choose number for delete todo: "))
        while user_number not in range(1, len(todos) + 1):
            print("Wrong number!!!")
            user_number = int(input("Please, choose number for deleting: "))
        todos.pop(user_number-1)
        print(f"Item with number {user_number} removed from file")
        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action == 'exit':
        break
    else:
        print("You entered unknown command!!!")

print('You end the program!!!')


