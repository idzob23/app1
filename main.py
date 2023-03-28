###You can also put prompt text into variable
###prompt='Enter a todo'
###user_text = input(prompt)
# todo1 = input("Enter a todo:")
# todo2 = input("Enter a todo:")
# todo3 = input("Enter a todo:")
#
# todo = [todo1, todo2, todo3]
#
# print(type(todo))
# print(todo)

############USE WHILE LOOP################
prompt='Enter a todo'
todo=[]
i=1
while i < 4:
    todo1 = input(prompt)
    todo.append(todo1)
    i += 1
print(todo)

