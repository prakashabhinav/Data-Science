# -*- coding: utf-8 -*-
"""
Udemy Course - Python Functions : 27-May-2019
"""
# Functions - To repeat a set of operations multiple times with different parameters
# Declared using def keyword
# No braces or brackets to specify the function, only indentation using white spaces

# Declaring a function to give the square of a number
def SquareIt(x):
    return x * x

# Calling the function to return the square of the number passed
print(SquareIt(2))
print(SquareIt(-4))

# Declaring a function to give the cube of a number
def CubeIt(x):
    return x * x * x

# Calling the function to return the square of the number passed
print(CubeIt(2))
print(CubeIt(-2))

# Functions - Pass functions around as parameters
# Declaring the function to pass function as parameters
def DoSomething(f, x):
    return f(x)

# Calling the function to pass function as parameters
print(DoSomething(SquareIt, 3))

# Declaring the function to pass function as parameters
def DoSomethingMore(f, x, f1, y):
    return (f(x),f1(y))
    
# Calling the function to pass function as parameters
print(DoSomethingMore(SquareIt, 3, CubeIt, 3))

# Functions - Lambda function allows us to inline simple functions
# Changes functionality of function at run time
# DoSomething function accepts a function in first parameter
# Lambda defines an unnamed function
print(DoSomething(lambda x: x * x * x, 3))
print(DoSomething(lambda x: x * x * x, -2))
print(DoSomething(lambda x: x, -2))

print(DoSomethingMore(lambda x: x * x, 2, lambda y: y * y * y, 2))
print(DoSomethingMore(lambda x: x * x, -2, lambda y: y * y * y, -2))
print(DoSomethingMore(lambda x: x * x, -2, lambda y: y * y * y, -3))

# Boolean Expressions
# == : Equals
# is : Equals (Python Specific)
# True
# False

# Examples
print(1 == 3)

print(2 == 2)

print(True or False)

print(True and False)

print(True and True)

print(1 is 3)

print(2 is 2)

print(True is False)

print(True or True)

# Another example
if 1 is 3:
    print("How did that happen?")
elif 1 > 3:
    print("Yikes")
else:
    print("All is well with the world")

# Another example
if 3 is 3:
    print("How did that happen?")
elif 1 > 3:
    print("Yikes")
else:
    print("All is well with the world")

# Another example
if 4 is 3:
    print("How did that happen?")
elif 4 > 3:
    print("Yikes")
else:
    print("All is well with the world")
    
# Looping - Repeat a set of operations for specific number of times
# Examples

# Print numbers in range using the Range function
for x in range(10):    # Prints number in the range of 0 to 9
    print(x)    

# Print numbers in range showing the use of Continue and Break statements
for x in range(10):
    if (x is 1):
        continue
    if (x > 5):
        break
    print(x)

# Use of while statement
x = 0
while (x < 10):
    print(x)
    x += 1    
    
# Activity - Write some code that creates a list of integers, loops through each element of the list, and only prints out even numbers 
listOfNumbers = [1, 2, 3, 16, 17, 4, 5, 6, 22, 26, 7, 8, 9, 10, 11, 12]
for number in listOfNumbers:
    if (number % 2 == 0):
        print(number)
    else:
        continue
print ("All done.")

## End of Practice ##