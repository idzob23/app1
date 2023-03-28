contents = ["All carrots are to be sliced "
            "longitudinally.",
            "The carrots will be reportedly sliced.",
            "The slicing process was well presented."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]
#####to put string into more than one line use  \
###For list no need for ]\
a = "I am Ilija" \
    "Bokan"



# for index, item in enumerate(contents):
#     file = open(filenames[index],"w")
#     file.write(item)
#     file.close
#
#2nd way
# >>> a=[1,2]
# >>> b=['a','b']
# >>> list(zip(a,b))
# [(1, 'a'), (2, 'b')]


for content, filename in zip(contents,filenames):
    file = open(filename, "w")
    file.write(content)
    file.close
