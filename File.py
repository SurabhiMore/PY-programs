fname = input("Enter file name: ")    # py4e_files(input)
fread = open(fname)          # content of file stored as string in fread
for words in fread:
    content = words.upper()  # uppercase words(of file content) stored as string in the variable
    print(content.rstrip())  # rstrip - to avoid space between two lines


