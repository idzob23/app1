user_input = input("Add e new member:")
file = open('members.txt', 'r')
members=file.readlines()
file.close()
members.append(user_input+"\n")

file = open('members.txt', 'w')
file.writelines(members)
file.close()

