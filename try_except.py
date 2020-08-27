# catching errors in python with try except
# there might be some situations where you program might throw and error or a bug messed with your code which might stop ur code from running. you need to prepare adeqautely for scenarios like these.

# number = int(input("Enter a Number: "))
# print(number)


# value = 10/0
 
try:
  value = 10/0
  number = int(input("Enter a Number: "))
  print(number)
except ValueError:
  print("Invalid input")
except ZeroDivisionError as err:
  print(err)  


# always except for a specific error. except without specificality is wrong
