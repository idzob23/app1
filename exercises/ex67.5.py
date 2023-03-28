for file in ["a.txt", "b.txt", "c.txt"]:
    f = open(file, 'r')
    text = f.read()
    print(text)
    f.close()