filename = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for file in filename:
    newfile = file.replace('.','-',1) #Replace only first occurence of '.'
    print(newfile)