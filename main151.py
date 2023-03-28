# ADD CURRENT TIME AND DATE AT THE BEGINNING OF THE SCRIPT

print("GIIIIIIT-HUBBBBBB............   ")

import functions
from datetime import datetime
DAY = datetime.now().strftime("%d")
MONTH = datetime.now().strftime("%b")
YEAR = datetime.now().strftime("%Y")
HOURS = datetime.now().strftime("%H")
MINUTES = datetime.now().strftime("%M")
SECONDS = datetime.now().strftime("%S")
print(f"It is {MONTH} {DAY}, {YEAR} {HOURS}:{MINUTES}:{SECONDS}")

################or######################
import time
now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}")


####PYTHON MODULE INDEX##############
#https://docs.python.org/3/py-modindex.html





todos = functions.get_todos()

while True:
    user_action = input("Type add, show, edit, delete or exit: ")

    if 'add ' in user_action or 'new ' in user_action:
        todo = user_action[len('add '):] + '\n'
        #todos = get_todos()
        todos.append(todo)

        functions.write_todos(todos)

    elif user_action in ('show','display'):

        #todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}. {item}")

    elif 'edit ' in user_action:
        try:
            user_number = int(user_action[len('edit '):])
            #todos = get_todos()
            while user_number not in range(1, len(todos) + 1):
                print("Wrong number!!!")
                user_action = input("Please, choose edit number for editing: ")
                user_number = int(user_action[5:])

            user_value = input("Enter new value: ") + "\n"

            todos[user_number - 1] = user_value
            functions.write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue    #no need for this

    #you can also use here IndexError instead while
    elif user_action.startswith('delete '):
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



            functions.write_todos(todos)
        except ValueError:#never be executed because I use while
            print("There is no todo with that number")

    elif user_action.startswith('exit'):
        break
    else:
        print("You entered unknown command!!!")

print('You end the program!!!')



