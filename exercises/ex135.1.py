def age(year_of_birth,current_year=2023):
    return current_year - year_of_birth


year_of_birth = int(input("What is your year of birth? "))
result = age(year_of_birth)

if result >= 121:
    print(f"You are {result} years old")
else:
    print("You are baby boy :-)")