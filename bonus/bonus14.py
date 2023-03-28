# Improve bonus13.py to sprreading content into different files
# Use PyCharm refactoring/move options
from bonus.converters14 import convert
from bonus.parsers14 import parse
# or
#from parsers14 import parse

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)

converted = convert(parsed[0], parsed[1])

if converted < 1:
    print("Kid is to small.")
else:
    print("Kid can use the slide")
