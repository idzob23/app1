import glob

# return filenames in particular dir with txt extension as list
myfiles = glob.glob("files/*.txt")

for filepath in myfiles:
    with open(filepath,'r') as file:
        print(filepath)
        print(file.read().upper())

