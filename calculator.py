# a basic calculator where we get 2 numbers from a user and we'll print the computation

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

result = int(num1) + int(num2)

# when we get input from a user by default, python would convert it into a string. we actually have to convert them to numbers using int() function which only deals with whole numbers

# if you want to compute floating numbers the int function will not work. you have to use float() which would compute a floating point number

print(result)