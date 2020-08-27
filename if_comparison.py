# comparison operators with if statements

# create a python fn that gives us the maximum number that's passed into it. its going to take in 3 numbers as input and print out the biggest number that we give it

def max_num(num1, num2, num3):
  if num1 >= num2 and num1 >= num3:
    return num1
  elif num2 >= num1 and num2 >= num3:
    return num2
  else:
    return num3


print(max_num(5,8,7))
