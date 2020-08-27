# one of the most common types of data that you're going to be working with in python is strings.

# strings are basically just plain text. any text that we're gonna have inside of program can be stored inside of a string.

# \ => escape character. it tells python that whatever character comes after it should be rendered literally.

# print("TechStudio\nAcademy")

# print("Techstudio\" Academy")

# string variable
# boot_camp = "Lambda School"
# print(boot_camp)

# concatenation => the process of taking a string and appending another string onto it
# boot_camp = "Lambda School"
# print(boot_camp + " offers a fullstack web dev program")

# functions
# a function is basically a little block of code that we can run and it'll perfom a specific operation for us.
# we can use functions to modify our strings and also get information about our strings.
boot_camp = "Lambda School"
print(boot_camp.lower())
print(boot_camp.upper())

# Return True if the string is an uppercase string, False otherwise.
print(boot_camp.isupper())
print(boot_camp.upper().isupper())

# Return the number of items in a container.
print(len(boot_camp))

# you can also get index of characters
print(boot_camp[0])

# the index fn will tell us where a specific character is located inside of our string
print(boot_camp.index("S"))

# Return a copy with all occurrences of substring old replaced by new.
print(boot_camp.replace("Lambda", "Techstudio"))