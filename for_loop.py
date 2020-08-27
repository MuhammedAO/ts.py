# a for loop is a special type of loop which allows us to loop over different collections of items.
# in for loops we specify a variable. this varible will represent a different value on each iteration
# each time, this variable will most likely have a different value
# for every letter in tsa, do something

for letter  in "TechStudio Academy":
  print(letter)
  
  
  
airlines = ["Air Peace", "Air France", "Emirates Airline"]  

for airline in airlines:
  print(airline)
  

for index in range(12):
  if index == 0:
    print("First iteration")
  else:
    print("Not First")  