todos = []

#print nicely (user friendly) list data
while True:
    user_action = input("Type add, show or exit: ")
    user_action = user_action.strip()

    if user_action == 'add':
        todo = input("Enter a todo: ")
        todos.append(todo)
        print(todos)
    elif user_action in ('show','display'):
        for item in todos:
            print(item)
    elif user_action == 'exit':
        break    #break is exit from loop.If you put quit this is the exit from program
    else:
        print("You entered unknown command!!!")

print('You end the program!!!')

