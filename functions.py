# "def" keyword is used to define a function in python

""" There are two types of function in python: user-defined functions and built-in functions

    Examples of built-in functions: print(), min(), max() etc.

    The following functions are examples of user-defined functions
 """

def printHelloWorld():
    print("Hello world")

printHelloWorld()


# we can use "pass" keyword to keep an incomplete function without any error

def incompleteFunction():
    pass        # This says the interpreter to just pass through this line quietly


# Passing Arguments to a function

""" 
There are four types of arguments that we can provide in a function:
        1. default arguments
        2. keyword arguments
        3. variable length arguments
        4. required arguments
 """

def calculateSum(a,b):
    print("The sum is",a+b)

# default arguments

def greet(name="steve"):    # Even if no argument is provided while calling, it will consider the default value of the argument (i.e. steve ). # if argument is provided, the default value is overridden 
    print("hello",name)

# keyword arguments

""" 
We can provide arguments with key=value, this way the interpreter recognizes the arguments by the parameter name.
    Hence,the order in which the arguments are passed does not matter.
    For example,
 """

calculateSum(b=3,a=1)   # as we are using keyword argument syntax, we can provide the arguments in any order

# required argument

""" 
If we don't provide default values to the parameters, the number of arguments passed while calling the function should
    exactly match the original function definition. Otherwise we get errors.
    
The order in which the arguments are passed also matters if we don't use key=value syntax.
    
"""

calculateSum(2,3)       # to call this function, we must pass two arguments

# Variable-length argument (two types)

# first type

def name(*name):      # The arguments passed while calling this function will be stored in the "name" tuple
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")

#second type

def name(**name):   # The key=value passed while calling this function will be stored in the "name" dictionary

    print("Hello,", name["fname"], name["mname"], name["lname"])    # we can access the "name" dictionary like this

name(mname = "Buchanan", lname = "Barnes", fname = "James")  # We must pass arguments using key=value syntax (and no need to maintain order)

# return statement

def returnVal():
    return "value"

print(returnVal())