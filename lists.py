# a lot of times when you're programming in python you're going to be dealing with large amounts of data and when you're dealing with large amount of data, you want to make sure you can manage and organize it properly

# a list is essentialy a structure that we can use inside of python to store lists of information. you can take a bunch of related data values and organize them inside of a list and then use it throughout your program. this makes keeping track of our data a lot easier.

# we create lists like we create variables in py. although with lists, the list name has to be as descriptive as it could be
# whenever you write this '[]', py knows u wanna create a list.

la_liga_teams = ["Barcelona", "Athletico Madrid", "Real Betis", "Eidbar", "Real Madrid"]

# accessing individual elements inside of a list
# -1 => starts at the back
# 1:  starts indexing from 1
# 1:3 grabs all the elements from 1 to 3 but not 3.
# modify la_liga_teams[4] = "Osasuna" 
print(la_liga_teams[1:3])