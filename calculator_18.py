# a better calculator
# convert input from string to a number using float


num1 = float(input("Enter first number: "))
operator = input("Choose an operator: ")
num2 = float(input("Enter second number: "))

if operator == "+":
  print(num1 + num2)
elif operator == "-":
  print(num1 - num2)
elif operator == "/":
  print(num1 / num2)    
elif operator == "*":
  print(num1 * num2)  
else:
  print("Invalid operator")    
  
