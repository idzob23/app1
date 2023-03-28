#todos = []

#store todos list to txt file
#but we always want do read existing data in a file and append moro todo
#readlines make a list but readlines make a string when reading a file content
#cannot read same file more than ones, because read is exhausted :-)
#use readline to read line by line
#we are using relative paths to open a file
#if we use absolute path than use r"" that will prevent converting \t into TAB
#file=open(r"D:\Tools\Python\Tkinter\PyCharmProjects\app1\venv\todos.txt","r")


while True:
    user_action = input("Type add, show, edit, delete or exit: ")
    user_action = user_action.strip()

    if user_action == 'add':
        file = open("todos.txt", "r")
        todos = file.readlines()                #this will make a list
        file.close()
        todo = input("Enter a todo: ") + "\n"   #because we want to store every input on different lines in txt file
        todos.append(todo)
        file = open("todos.txt", "w")
        file.writelines(todos)
        file.close()
    elif user_action in ('show','display'):
        #read from file
        file = open("todos.txt", "r")
        todos = file.readlines()
        file.close()
        for index, item in enumerate(todos):
            item = item.replace("\n","")       #remove \n from list items, you can use item.strip('\n')
            #2nd way is list comprehensions, which remove \n from all list item
            #new_item = [item.strip('\n') for item in todos]
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
