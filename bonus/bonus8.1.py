

#Put results in dict
result={'length':False, 'digit':False, 'upper-case':False}
user_input = input("Enter new password: ")
if len(user_input) >= 8:
    result['length'] = True

    for i in user_input:
        if i.isdigit():
            result['digit'] = True
            break


    for i in user_input:
        if i.isupper():
            result['upper-case'] = True
            break

#print(result)
if all(result.values()) == True:
    print("Strong password")
else:
    print("Weak password")

