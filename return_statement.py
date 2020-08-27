# most times when we call a function, we would, often times than not, want to get back information from that function

# we'll write a little function that will cube a number. when we cube a number, we take it to the power of 3.

# Python relies on indentation (whitespace at the beginning of a line) to define scope in the code. Other programming languages often use curly-brackets for this purpose.

def cube_a_number(num):
   return num * num * num
        
# you also cannot run any code after the return statement
print(cube_a_number(3))    
