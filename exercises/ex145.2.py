# In coding exercise 1, we hardcoded the values 0 and 100. It is better to change them to constants in the script where the function is defined.
# Therefore, your task is to modify the script from exercise 1 by creating two global variables/constants in that file,
# one variable associated with 0 and another associated with 100.
# Then, use those variables in the function instead of the values.


from waterstate2 import water_state


user_input = float(input("Enter water temperature: "))
result  = water_state(user_input)
print(result)


