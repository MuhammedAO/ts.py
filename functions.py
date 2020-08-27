# a function is a collection of code which performs a specific task
# A function is a block of code which only runs when it is called.
# functions allow you to organize your code a lot better. they allow you to break up your code into chunks that are doing different things.

# we use the 'def' keyword when we want to declare fns in py.
# py will treat everything that comes after the : as our function block.
# in order to write code that belongs to the block, we need to indent.

def hello_world(language):
    print("Hello World from " + language)
    print("I love python")
    
hello_world("Python")
hello_world("javaScript")
# the code inside of a fn will only get executed when we specifiy that we want to execute it i.e invoking the fn.
# your functions should be named in all lowercase.


# we can make our functions a little more powerful by passing them information. these additional informations are called parameters
# so a parameter is a piece of information that we give to the function