question="Please enter your country origin?"

while True:
    user_input = input(question)

    if user_input == 'USA':
        print('Hello')
    elif user_input == 'India':
        print('Namaste')
    elif user_input == 'Germany':
        print('Hallo')
    else:
        print("Another exercise")
        ingredients = ["john smith", "sen plakay", "dora ngacely"]
        for i in ingredients:
            print(i.title())
        break

