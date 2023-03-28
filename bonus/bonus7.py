filenames = ['1.doc', '1.report', '1.presentation']
#transfer this list to ['1-doc.txt', '1-report.txt', '1-presentation.txt']

new_filenames = [item.replace('.', '-')+'.txt' for item in filenames]
print(new_filenames)

