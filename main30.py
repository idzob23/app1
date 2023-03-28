todos = []

# Python 3.9 have not match function
# while True:
#     user_action = input("Type add or show: ")
#     match user_action:
#         case 'add':
#             todo = input("Enter a todo: ")
#             todos = todos.append(todo)
#         case 'show':
#             print(todos)


while True:
    user_action = input("Type add, show or exit: ")
    if user_action == 'add':
        todo = input("Enter a todo: ")
        todos.append(todo)
        print(todos)
    elif user_action == 'show':
        print(todos)
    elif user_action == 'exit':
        break    #break is exit from loop.If you put quit this is the exit from program

print('You end the program!!!')


