ips = ['100.122.133.105', '100.122.133.111']


while True:
    user_choice = input("Enter the index of the IP you want:")
    if int(user_choice) not in [0,1]:
        print("Please enter 0 or 1")
    else:
        print(f"You chose {ips[int(user_choice)]}")
        break


