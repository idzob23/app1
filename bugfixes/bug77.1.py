# The code below tries
# to write the items of temperatures each in one line in the file.txt list.However, the
# code has an err fix the error.

# temperatures = [10, 12, 14]
#
# file = open("file.txt", 'w')
# 
# file.writelines(temperatures)

temperatures = [10, 12, 14]
file = open("file.txt", 'w')
new_temperatures = [str(item) + '\n' for item in temperatures]
file.writelines(new_temperatures)
file.close()