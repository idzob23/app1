#Eliminate the error
# def get_maximum():
#     celsius = [14, 15.1, 12.3]
#     maximum = max(celsius)
#     print(maximum)
#
#
# celsius = get_maximum()
#
# fahrenheit = celsius * 1.8 + 32
# print(fahrenheit)
# TypeError: unsupported operand type(s) for *: 'NoneType' and 'float'
def get_maximum():
    celsius = [14, 15.1, 12.3]
    maximum = max(celsius)
    return maximum


celsius = get_maximum()

fahrenheit = celsius * 1.8 + 32
print(fahrenheit)
