# -*- coding: utf-8 -*-
"""
Udemy Course - Conditional Probability : 06-Sep-2019
"""
# Conditional Probability - Way to measure the relationship of two things happening  in relation to each other
# Conditional Probability - If we have two events that depend on each other, what's the probability that both will occur
# Conditional Probability - Notation : P(A,B) is the probability of A and B both occurring independent of each other
# Conditional Probability - Notation : P(B|A) is the probability of B given that A has occurred
# Conditional Probability - P(B|A) = P(A,B) / P(A)

# Conditional Probability - Example
# Code to create some fake data on how much stuff people purchase given their age range.
# It generates 100,000 random "people" and randomly assigns them as being in their 20's, 30's, 40's, 50's, 60's, or 70's.
# It then assigns a lower probability for young people to buy stuff.
# In the end, we have two Python dictionaries:
# "totals" contains the total number of people in each age group.
# "purchases" contains the total number of things purchased by people in each age group.
# The grand total of purchases is in totalPurchases, and we know the total number of people is 100,000.

# Import required libraries
from numpy import random                           # Imports random method from numpy

# Setting the random seed
random.seed(0)                                     # Setting the random seed to generate random numbers
totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}      # Creating dictionary for random totals
purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}   # Creating dictionary for random purchases
totalPurchases = 0                                 # Initializing totalPurchases
# random.random() function                         # Generates random float uniformly in the semi-open range [0.0, 1.0)
# random.choice() function                         # Returns a random element from the non-empty sequence like from a list, Set, Dictionary
for _ in range(100000):                            # Loop to generate random values
    ageDecade = random.choice([20, 30, 40, 50, 60, 70])  # Sorting 100,000 age values into different age groups
    purchaseProbability = float(ageDecade) / 100.0       # Deciding probability based on the age groups
    totals[ageDecade] += 1                               # Taking total of age groups
    if (random.random() < purchaseProbability):          # Comparing probabilities by generating random probabilities through random
        totalPurchases += 1                              # Taking total of purchases
        purchases[ageDecade] += 1                        # Taking total of purchases in a decade

# Display variable values
totals                                                   # Display the total population in each age group (decade)

purchases                                                # Display the total purchases in each age group (decade)

totalPurchases                                           # Display the total purchases

