# -*- coding: utf-8 -*-
"""
Udemy Course - Covariance and Correlation : 31-Aug-2019
"""
# Covariance and Correlation - Ways to measure whether two attributes are related to each other in a dataset
# Covariance - Measures how two variables vary in tandem from their means
# Covariance - Interpreting covariance is hard, so we use correlation
# Covariance - Magnitude which matters, +ve or -ve just shows the type of covariance
# Correlation - Divide the covariance by the standard deviations of both variables and that normalizes the things
# Correlation - Correlation of - 1 : Perfect inverse correlation
# Correlation - Correlation of 0   : No correlation
# Correlation - Correlation of + 1 : Perfect correlation
# Correlation does not imply causation,it is used to decide what experiments to conduct


# Covariance and Correlation
# Covariance withour using the numpy methods
# Import required libraries
import numpy as np                                 # Makes calculation of Mean, Median, Mode, Standard Deviation, Variance
import matplotlib.pyplot as plt                    # Makes graphs for visualisation

# Define the function to calculate the deviations from mean for a set of values
def de_mean(x):                                    # Function to calculate the deviation from mean
    xmean = np.mean(x)                             # Calculating the mean
    return[xi - xmean for xi in x]                 # Return the list with the deviations form the mean
    
# Define the function to calculate the covariance
def covariance(x, y):                              # Function to calculate the covariance
    n = len(x)                                     # Calculate the length of the list 
    return np.dot(de_mean(x), de_mean(y)) / (n- 1) # Calculating the covariance

pageSpeeds = np.random.normal(3.0, 1.0, 1000)      # Generate random numbers for pageSpeeds with normal distribution; mu = 3.0, sigma = 1.0
purchaseAmount = np.random.normal(50.0, 10.0, 1000)  # Generate random numbers for purchaseAmount with normal dist.; mu = 50, sigma = 10

plt.scatter(pageSpeeds, purchaseAmount)            # Create scatter plot for pageSpeeds and purchaseAmount

covariance(pageSpeeds, purchaseAmount)             # Calculate covariance using the user defined function to calculate covariance
    
# We will now try to introduce a relationship between purchaseAmount and pageSpeeds and induce a correlation
# It will show a negative value meaning that pages that render in less time result in more money spent
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds  # Introducing -ve relationship between purchaseAmounts and pageSpeeds

plt.scatter(pageSpeeds, purchaseAmount)            # Create scatter plot for pageSpeeds and purchaseAmount which shows a relationship

covariance(pageSpeeds, purchaseAmount)             # Calculate covariance using the user defined function to show the covariance

# Numpy can be used to do this easily using the function numpy.cov
# numpy.cov returns a matrix of the covariance values between every combination of the array values
np.cov(pageSpeeds, purchaseAmount)                 # Gives covariance value similar to the values returned by the function

# Covariance value or Magnitude which matters, +ve or -ve just shows the type of covariance
# Covariance is sensitive to units used in the variables, which makes it difficult to interpret
# Correlation normalizes everything by using the standard deviations
# Correlation gives us easier values that range from -1 (Perfect InverseCorrelation) to +1 (Perfect Correlation)

# Define the function to calculate the correlation
def correlation(x, y):                             # Function to calculate the covariance
    stddevx = x.std()                              # Calculate the standard deviation of x values
    stddevy = y.std()                              # Calculate the standard deviation of x values
    return covariance(x, y) / stddevx / stddevy    # Check for divide by zero here and then return the correlation value 

correlation(pageSpeeds, purchaseAmount)            # Calculate correlation using the user defined function to calculate correlation

# Numpy can be used to do this easily using the function numpy.corrcoef
# numpy.corrcoef returns a matrix of the correlation coefficients between every combination of the array values
np.corrcoef(pageSpeeds, purchaseAmount)            # Gives correlation value similar to the values returned by the function

# Show positive relationship, covariance and correlation
purchaseAmount = np.random.normal(50.0, 10.0, 1000) * pageSpeeds  # Introducing +ve relationship between purchaseAmounts and pageSpeeds

plt.scatter(pageSpeeds, purchaseAmount)            # Create scatter plot for pageSpeeds and purchaseAmount which shows a relationship

covariance(pageSpeeds, purchaseAmount)             # Calculate covariance using the user defined function to show the covariance

np.cov(pageSpeeds, purchaseAmount)                 # Gives covariance value similar to the values returned by the function

correlation(pageSpeeds, purchaseAmount)            # Calculate correlation using the user defined function to calculate correlation

np.corrcoef(pageSpeeds, purchaseAmount)            # Gives correlation value similar to the values returned by the function

# Check for a perfect correlation by fabricating a totally linear relationship : -ve correlation
purchaseAmount = 100 - pageSpeeds * 3              # Introducing a linear relationship between purchaseAmounts and pageSpeeds

plt.scatter(pageSpeeds, purchaseAmount)            # Create scatter plot for pageSpeeds and purchaseAmount which shows a relationship

correlation(pageSpeeds, purchaseAmount)            # Calculate correlation using the user defined function to calculate correlation

np.corrcoef(pageSpeeds, purchaseAmount)            # Gives correlation value similar to the values returned by the function

# Check for a perfect correlation by fabricating a totally linear relationship : +ve correlation
purchaseAmount = 100 + pageSpeeds * 3              # Introducing a linear relationship between purchaseAmounts and pageSpeeds

plt.scatter(pageSpeeds, purchaseAmount)            # Create scatter plot for pageSpeeds and purchaseAmount which shows a relationship

correlation(pageSpeeds, purchaseAmount)            # Calculate correlation using the user defined function to calculate correlation

np.corrcoef(pageSpeeds, purchaseAmount)            # Gives correlation value similar to the values returned by the function

## End of Practice ##