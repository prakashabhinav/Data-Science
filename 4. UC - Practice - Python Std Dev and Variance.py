# -*- coding: utf-8 -*-
"""
Udemy Course - Python Basics Std Dev and Var : 28-May-2019
"""
# Standard Deviation and Variance
# Variance - Measures how "spread out" the data is
# Variance - Average of the squared differences from the mean
# Standard Deviation - Square root of the variance
# Variance and Standard Deviation - Helps to identify outliers
# Population Mean : μ = ( Σ Xi ) / N
# Population Variance : σ2
# Sample Mean : M = ( Σ Xi ) / N
# Population and Sample 
# Population Variance uses N, Sample Variance uses N- 1

# Import required libraries
import numpy as np                                 # Makes calculation of Mean, Median, Mode, Standard Deviation, Variance
import matplotlib.pyplot as plt                    # Makes graphs for visualisation

# Generate random income numbers - Set 1
incomes = np.random.normal(100.0, 20.0, 10000)     # Generate random income numbers

# Segment the income data into 50 buckets, and plot it as a histogram
plt.hist(incomes, 50)                              # Segments the data into 50 buckets
plt.show()                                         # Display the histogram    

# Calculate Standard Deviation
incomes.std()                                      # Display the standard deviation

# Calculate Variance 
incomes.var()                                      # Display the variance

# Generate random income numbers - Set 2
incomes = np.random.normal(100.0, 50.0, 10000)     # Generate random income numbers

# Segment the income data into 50 buckets, and plot it as a histogram
plt.hist(incomes, 50)                              # Segments the data into 50 buckets
plt.show()                                         # Display the histogram    

# Calculate Standard Deviation
incomes.std()                                      # Display the standard deviation

# Calculate Variance 
incomes.var()                                      # Display the variance

# Generate random income numbers - Set 3
incomes = np.random.normal(100.0, 75.0, 10000)     # Generate random income numbers

# Segment the income data into 50 buckets, and plot it as a histogram
plt.hist(incomes, 50)                              # Segments the data into 50 buckets
plt.show()                                         # Display the histogram    

# Calculate Standard Deviation
incomes.std()                                      # Display the standard deviation

# Calculate Variance 
incomes.var()                                      # Display the variance

## End of Practice ##