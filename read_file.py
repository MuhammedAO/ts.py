# reading from external file

# mode => read, write(w), append(a), rea&write(r+)

notes = open("notes.md", "r")

# whenever you open a file, u always wanna make sure u close the file.
# u also need to check if the file is readble
print(notes.read())
print(notes.readlines())
# print(notes.readline())
# print(notes.readline())

notes.close()