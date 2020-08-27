# 'if' statements are a structure in python that allows us to help our programs make decisions
# by using if statements, we could execute a certain part of our code is certain conditions true 
# basically if statements allow our programs respond to the input that they are given

# if statements are something if we as humans deal with all of the time. as you go through your day, you're executing if statements
# elif for elseif
#not() => negation 


# basic example

is_male = True
is_nigerian = False

if is_male and is_nigerian:
  print("I'm a laze yute from nigeria")
elif is_male and not(is_nigerian):
  print("You're not one of us")  
else:
  print("i'm a hard working yute")