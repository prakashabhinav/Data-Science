# -*- coding: utf-8 -*-
"""
Udemy Course - Python Basics : 26-May-2019
"""
# For Loop example
listOfNumbers = [1, 2, 3, 4, 5, 6]
for number in listOfNumbers:
    print(number)
    if (number % 2 == 0):
        print("is even")
    else:
        print("is odd")
print ("All done.")

# Importing Modules 
# Importing numpy package (Numpy ~ Numeric Python)
import numpy as np

# Generating random numbers : Calling random function and generating the normal distribution
a = np.random.normal(25.0, 5.0, 10)
print (a)

b = np.random.normal(5.0, 25.0, 10)
print (b)

# Working with Lists
# Lists are mutable : Add items to list and rearrange items
# Square brackets [ ] indicate a python list 
# We can add any type of data to a list
x = [1,2,3,4,5,6]
print (len(x))

y = [1,2,3,4,5,6,'a']
print (len(y))

# List - Slicing and Dicing
# Select anything before element number 3
x[:3]

# Select anything before element number 4
x[:4]

# Select anything after element number 3
x[3:]

# Select anything after element number 4
x[4:]

# Select two elements from last element
x[-2:]

# Select all elements from last two elements
x[:-2]

# Add more elements to the existing list in the form of list
x.extend([7,8])
x

# Add more element to the existing list in the form of single character
x.append(9)
x

x.append([10,11])
x

# Adding a list to an existing list : Merges both the lists and creates a new list
y = [12, 13, 14]
listOfLists = [x,y]                 # Merges both the lists
listOfLists                         # Shows both the lists througn the merged list

# Select second element of list y
y[1]

# Select second element of list listOfLists
listOfLists[1]

# Sorting Lists - Ascending Order
z = [3 ,2 , 1]
z.sort()
z

# Sorting Lists - Ascending Order : Another example
zs = [1,3,5,7,9,2,4,6,8,10]
zs.sort()
zs

# Sorting Lists - Descending Order
z = [3 ,2 , 1]
z.sort(reverse=True)
z

# Sorting Lists - Descending Order : Another example
zs = [1,3,5,7,9,2,4,6,8,10]
zs.sort(reverse=True)
zs

# Working with Tuples
# Tuples are immutable : We can not change them, they are what they are
# Round brackets ( ) indicate a python tuple 
x = (1,2,3)                       # Defining a tuple
len(x)                            # Display the length of a tuple

y = (4,5,6)                       # Defining a tuple
y[0]                              # Display first element of a tuple - Count starts from 0
y[1]                              # Display second element of a tuple - Count starts from 0
y[2]                              # Display third element of a tuple - Count starts from 0
y[3]                              # Gives index out of range error

# Creating a list from tuples
listofTuples = [ x , y ]          # Defining a list of tuples
listofTuples                      # Display the list of tuples

# Moving values to a tuple from an input data stream
# Split the input data stream based on a delimiter with the help of split function
(age, income) = "32,12000".split(',')  # Defining an input data stream and split it by split function
print(age)                             # Display the first element
print(income)                          # Display the second element

# Working with Dictionary
# Like a map or hash table in other languages, like a mini database
# Key value mapping datastore
# Round brackets { } indicate a python dictionary
captains = {}                          # Defining a blank dictionary
captains["Enterprise"] = "Kirk"        # Defining dictionary element
captains["Enterprise D"] = "Picard"    # Defining dictionary element
captains["Deep Space Nine"] = "Sisko"  # Defining dictionary element
captains["Voyager"] = "Janeway"        # Defining dictionary element

print(captains["Voyager"])             # Display dictionary element

print(captains.get("Enterprise"))      # Display dictionary element - Another way
print(captains.get("Voyager"))         # Display dictionary element - Another way

print(captains.get("NX-01"))           # Display error message

# Using for loop to display all elements of the dictionary
for ship in captains:                  # For loop
    print(ship + ": " + captains[ship])# Display the dictionary elements
    
## End of Practice ##