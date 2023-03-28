#Optimising code from main82.py

#Allow user to enter "add  Play Chess"
#Check if add exist and remove it from user_input

#Boolean data types:    True and False
#Boolean operators:     and, or, ....
#Add new as alternative to add
with open('todos.txt', 'r') as file:
    todos = file.readlines()

while True:
    user_action = input("Type add, show, edit, delete or exit: ")

    if 'add ' in user_action or 'new ' in user_action:
        todo = user_action[len('add '):] + '\n'
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action in ('show','display'):

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")

    elif 'edit ' in user_action:
        try:
            user_number = int(user_action[len('edit '):])
            while user_number not in range(1, len(todos) + 1):
                print("Wrong number!!!")
                user_action = input("Please, choose edit number for editing: ")
                user_number = int(user_action[5:])

            user_value = input("Enter new value: ") + "\n"
            todos[user_number - 1] = user_value
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        except ValueError:
            print("Your command is not valid")
            continue    #no need for this

    #you can also use here IndexError instead while
    elif 'delete ' in user_action:
        try:
            user_number = int(user_action[len('delete '):])
            while user_number not in range(1, len(todos) + 1):
                print("Wrong number, use number between 1 and " + str(len(todos)) +" !!!")
                user_action = input("Please, choose delete number for delete todo: ")
                user_number = int(user_action[7:])

            todos.pop(user_number - 1)
            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index + 1}. {item}")



            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("There is no todo with that number")

    elif 'exit' in user_action:
        break
    else:
        print("You entered unknown command!!!")

print('You end the program!!!')


