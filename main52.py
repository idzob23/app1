todos = []


while True:
    user_action = input("Type add, show, edit, delete or exit: ")
    user_action = user_action.strip()

    if user_action == 'add':
        todo = input("Enter a todo: ")
        todos.append(todo)
        print(todos)
    elif user_action in ('show','display'):
        for index, item in enumerate(todos):
            print(f"{index + 1}. {item}")
    elif user_action == 'edit':
        for index, item in enumerate(todos):
            print(f"{index+1}. {item}")
        user_number = int(input("Please, choose number for editing: "))
        while user_number not in range(1, len(todos) + 1):
            print("Wrong number!!!")
            user_number = int(input("Please, choose number for editing: "))
        user_value = input("Enter new value: ")
        todos[user_number-1] = user_value
    elif user_action == 'delete':
        for index, item in enumerate(todos):
            print(f"{index + 1}. {item}")
        user_number = int(input("Please, choose number for delete todo: "))
        todos.pop(user_number-1)
    elif user_action == 'exit':
        break    #break is exit from loop.If you put quit this is the exit from program
    else:
        print("You entered unknown command!!!")

print('You end the program!!!')


####################3 ways to show numbered list#####################
# for i in range(1, len(todos) + 1):
#     print(str(i) +'. ' + str(todos[i-1]))

# for i in todos:
#     print(str(todos.index(i) + 1) + '. ' + str(i))
##############most elegant way
# for index, item in enumerate(todos):
#     print(str(index+1)  + '. ' + str(item))
#     print(f"{index+1}. {item}")
#########WHEN USING + ALWAYS PUT STR BEACAUSE LIST MEMBERS CAN BE NUMBERS, OR USE "," WHICH ADD EXTRA SPACE
#######BEST WAY IS TO USE F-STRINGS, NO STR CONVERSION AND YOU CAN CONTROL SPACES
######## print(f"{index+1}. {item}")
