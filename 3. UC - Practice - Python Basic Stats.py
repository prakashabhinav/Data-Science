# -*- coding: utf-8 -*-
"""
Udemy Course - Python Basic Stats : 27-May-2019
"""
# Types of Data : Numerical, Categorical, Ordinal
# Numerical : Discrete, Continuous
# Categorical : Yes/No, Male/Female
# Ordinal : Mix of Numerical and Categorical Data
# Mean, Median, and Mode
# Mean   : Average value, Sum of values / Number of samples
# Median : Sort the values and take the value at midpoint. If there are even number of values, take the average of two values in the middle
# Median : Less susceptible to outliers than the mean
# Mode   : Most common value in a dataset with discrete values
# Mean vs. Median

# Create sample income data, centered around 27,000 with a normal distribution and standard deviation of 15,000, with 10,000 data points
# Compute the mean (average) - it should be close to 27,000

# Import required libraries
import numpy as np                                 # Makes calculation of Mean, Median and Mode easy
import matplotlib.pyplot as plt                    # Makes graphs for visualisation
from scipy import stats                            # Used for stats mode function

# Generate random income numbers
# import numpy as np                               # Makes calculation of Mean, Median and Mode easy
incomes = np.random.normal(27000, 15000, 10000)    # Generate random income numbers
len(incomes)                                       # Display count of random income numbers
np.mean(incomes)                                   # Display mean of random income numbers

# Segment the income data into 50 buckets, and plot it as a histogram
# import matplotlib.pyplot as plt                  # Makes graphs for visualisation - Used in beginning of code
plt.hist(incomes, 50)                              # Segments the data into 50 buckets
plt.show()                                         # Display the histogram

# Compute the median
np.median(incomes)                                 # Display the median of random income numbers
# Since we have a normal distribution, Mean and Median and pretty close and near to each other

# Now, we add an outlier
incomes = np.append(incomes, [1000000000])         # Adding outlier to bring skewness in the data 

np.median(incomes)                                 # Display the median of random income numbers with skewness
np.mean(incomes)                                   # Display mean of random income numbers with skewness
# Adding an outlier changes the Mean drastically, where as Median remains almost the same
# Thus, when there are outliers in the data or the data is skewed, Median should be used

# Mode
# Generate sample age data for 500 people
ages = np.random.randint(18, high=90, size=500)    # Generate random age data
ages                                               # Display random age data 

# from scipy import stats                          # Used for stats mode function - Used in the beginning of code
stats.mode(ages)                                   # Display the mode for sample age data

# Exercise: Mean & Median Customer Spend
custspend = np.random.normal(100.0, 20.0, 10000)   # Generate random customer spend numbers
len(custspend)                                     # Display count of random customer spend numbers
np.mean(custspend)                                 # Display mean of random customer spend numbers

# Segment the customer spend data into 50 buckets, and plot it as a histogram
# import matplotlib.pyplot as plt                  # Makes graphs for visualisation - Used in beginning of code
plt.hist(custspend, 50)                              # Segments the data into 50 buckets
plt.show()                                         # Display the histogram

# Compute the median
np.median(custspend)                               # Display the median of random customer spend numbers
# Since we have a normal distribution, Mean and Median and pretty close and near to each other

# Now, we add an outlier
custspend = np.append(custspend, [100000])         # Adding outlier to bring skewness in the data 

np.median(custspend)                               # Display the median of random customer spend numbers with skewness
np.mean(custspend)                                 # Display mean of random customer spend numbers with skewness
# Adding an outlier changes the Mean drastically, where as Median remains almost the same
# Thus, when there are outliers in the data or the data is skewed, Median should be used

## End of Practice ##