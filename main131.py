#Default function parameter.
#If we have more than one parameters default one must be at the end
#get_todos I have couple of times...It is better to read list on program start
#you need to declare global variable if you want to call it inside function

#DOCSTRINGS
#You can create your own docstring
#You can also use it to enter multiline text

text="""
Hello, this is my very
first program.
I hope that you are enjoy it. :-)
"""
print(text)

def get_todos(filepath="todos.txt"):
    """ Read the text file and return
        the list of to-do items
    """
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todo_list, filepath='todos.txt'):
    """ Write the list items in text file"""
    with open(filepath, 'w') as file:
        file.writelines(todo_list)



todos = get_todos()

while True:
    user_action = input("Type add, show, edit, delete or exit: ")

    if 'add ' in user_action or 'new ' in user_action:
        todo = user_action[len('add '):] + '\n'
        #todos = get_todos()
        todos.append(todo)

        write_todos(todos)

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
            write_todos(todos)

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



            write_todos(todos)
        except ValueError:#never be executed because I use while
            print("There is no todo with that number")

    elif user_action.startswith('exit'):
        break
    else:
        print("You entered unknown command!!!")

print('You end the program!!!')



