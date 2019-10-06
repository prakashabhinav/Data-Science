# -*- coding: utf-8 -*-
"""
Udemy Course - Probability Density Function and Probability Mass Function : 30-Aug-2019
"""
# Probability Density Function and Probability Mass Function
# Probability Density Function : For Continuous Data, an example is the Normal distribution
# Probability Density Function : Gives the probability of a data point falling within some given range of a given value
# Normal Distribution : -1 SD to +1 SD : 68.2 Percent
# Normal Distribution : -2 SD to +2 SD : 95.4 Percent
# Normal Distribution : -3 SD to +3 SD : 99.6 Percent
# Probability Mass Function : For Discrete Data
# Probability Density Function : Gives the probability of a data point falling within some given range of a given value
# Normal Distribution : -1 SD to +1 SD : 68.2 Percent
# Normal Distribution : -2 SD to +2 SD : 95.4 Percent
# Normal Distribution : -3 SD to +3 SD : 99.6 Percent

# Probability Density Functions
# Distributions for Probability Density Functions
# Import required libraries
import numpy as np                                 # Makes calculation of Mean, Median, Mode, Standard Deviation, Variance
import matplotlib.pyplot as plt                    # Makes graphs for visualisation

# Uniform Distribution - Flat, constant probability 
# Uniform Distribution - Equal chance of a value occuring within a given range
# Uniform Distribution Probability Distribution Function
# Generate random numbers with uniform distribution - Set 1
values = np.random.uniform(-10.0, 10.0, 100000)    # Generate random numbers with uniform distribution

# Segment the income data into 50 buckets, and plot it as a histogram
plt.hist(values, 50)                               # Segments the data into 50 buckets
plt.show()                                         # Display the histogram

# Calculate Standard Deviation
values.std()                                       # Display the standard deviation

# Calculate Variance 
values.var()                                       # Display the variance

# Generate random numbers with uniform distribution - Set 2
values = np.random.uniform(100.0, 50.0, 100000)    # Generate random numbers with uniform distribution

# Segment the income data into 50 buckets, and plot it as a histogram
plt.hist(values, 50)                               # Segments the data into 50 buckets
plt.show()                                         # Display the histogram

# Calculate Standard Deviation
values.std()                                       # Display the standard deviation

# Calculate Variance 
values.var()                                       # Display the variance

# Normal / Gaussian Distribution - Bell curve PDF
# Normal / Gaussian Disribution Probability Distribution Function
# Import required libraries
from scipy.stats import norm                       # Provides pdf function to create probability density function for normal distribution
import matplotlib.pyplot as plt                    # Makes graphs for visualisation

# Generate random numbers in the specified range with a step value of 0.001 - Set 1
x = np.arange(-3, 3, 0.001)                        # Generate random numbers within -3 to + 3 with an increment of 0.001

# Plot the normal distribution curve
plt.plot(x, norm.pdf(x))                           # Display the normal distribution curve

# Generate random numbers in the specified range with a step value of 0.001 - Set 2
x = np.arange(-5, 15, 0.001)                       # Generate random numbers within -5 to + 15 with an increment of 0.001

# Plot the normal distribution curve
plt.plot(x, norm.pdf(x))                           # Display the normal distribution curve

# Normal Distribution Probability Distribution Function
# Generate random numbers with normal distribution, "mu" is the desired mean and "sigma" is the standard deviation - Set 1
# Import required libraries
import numpy as np                                 # Makes calculation of Mean, Median, Mode, Standard Deviation, Variance
import matplotlib.pyplot as plt                    # Makes graphs for visualisation

mu = 5.0                                           # Desired mean value
sigma = 2.0                                        # Desired standard deviation value

values = np.random.normal(mu, sigma, 10000)        # Generate random numbers with the provided mean and standard deviation values

# Segment the income data into 50 buckets, and plot it as a histogram
plt.hist(values, 50)                               # Segments the data into 50 buckets
plt.show()                                         # Display the histogram    
# Curve will not be the actual normal distribution curve as the numbers are still random

# Generate random numbers with normal distribution, "mu" is the desired mean and "sigma" is the standard deviation - Set 2
mu = 15.0                                          # Desired mean value
sigma = 50.0                                       # Desired standard deviation value

values = np.random.normal(mu, sigma, 10000)        # Generate random numbers with the provided mean and standard deviation values

# Segment the income data into 50 buckets, and plot it as a histogram
plt.hist(values, 50)                               # Segments the data into 50 buckets
plt.show()                                         # Display the histogram    
# Curve will not be the actual normal distribution curve as the numbers are still random

# Exponential Probability Distribution Function / Power Law - Falls off in an exponential manner, 
# Exponential Probability Distribution Function / Power Law - Probability Very likely for something to happen near Zero
# Exponential Probability Distribution Function / Power Law - Probability drops off as wemove away from Zero
# Import required libraries
from scipy.stats import expon                      # Provides pdf function to create probability density function for exponential dist
import matplotlib.pyplot as plt                    # Makes graphs for visualisation

# Generate random numbers in the specified range with a step value of 0.001 - Set 1
x = np.arange(0, 10, .001)                         # Generate random numbers within 0 to + 10 with an increment of 0.001

# Plot the exponential distribution curve
plt.plot(x, expon.pdf(x))                          # Display the exponential distribution curve
# Exponential curve from 0 to 10 on X-Axis with probability 1 near Zero

# Generate random numbers in the specified range with a step value of 0.001 - Set 2
x = np.arange(5, 10, .001)                         # Generate random numbers within + 5 to + 10 with an increment of 0.001

# Plot the exponential distribution curve
plt.plot(x, expon.pdf(x))                          # Display the exponential distribution curve
# Exponential curve from 5 to 10 on X-Axis

# Generate random numbers in the specified range with a step value of 0.001 - Set 3
x = np.arange(-5, 0, .001)                         # Generate random numbers within - 5 to 0 with an increment of 0.001

# Plot the exponential distribution curve
plt.plot(x, expon.pdf(x))                          # Display the exponential distribution curve
# No Exponential curve from - 5 to 0 on X-Axis, only a straight line with Zero probability

# Generate random numbers in the specified range with a step value of 0.001 - Set 4
x = np.arange(-5, 5, .001)                         # Generate random numbers within - 5 to + 5 with an increment of 0.001

# Plot the exponential distribution curve
plt.plot(x, expon.pdf(x))                          # Display the exponential distribution curve
# No Exponential curve from - 5 to 0 on X-Axis, only a straight line with Zero probability
# No Exponential curve at 0 on X-Axis, only a straight line with One probability
# Exponential curve from 0 to + 5 on X-Axis

# Probability Mass Functions - Deal with discrete data
# Distributions for Probability Mass Functions
# Binomial Distribution Probability Mass Function
# Import required libraries
from scipy.stats import binom                      # Provides pmf function to create probability mass function for binomial dist     
import matplotlib.pyplot as plt                    # Makes graphs for visualisation

# Generate random numbers in the specified range with a step value of 0.001 - Set 1
x = np.arange (0, 10, 0.001)                       # Generate random numbers within 0 to + 10 with an increment of 0.001

# Shape parameters for creating the plot
n, p = 10, 0.5                                     # Shape parameters for the binomial distribution curve

# Plot the binomial distribution curve
plt.plot(x, binom.pmf(x, n, p))                    # Display the binomial distribution curve

# Generate random numbers in the specified range with a step value of 0.001 - Set 2
x = np.arange (0, 10, 0.001)                       # Generate random numbers within 0 to + 10 with an increment of 0.001

# Shape parameters for creating the plot
n, p = 20, 0.5                                     # Shape parameters for the binomial distribution curve

# Plot the binomial distribution curve
plt.plot(x, binom.pmf(x, n, p))                    # Display the binomial distribution curve

# Poisson Distribution Probability Mass Function
# Poisson Distribution - If we have some average number of things for a given period
# Poisson Distribution - Gives a way to predict other values for another given day
# Poisson Distribution - Example : A website gets on average 500 visits per day, what's the odds of getting 550
# Import required libraries
from scipy.stats import poisson                    # Provides pmf function to create probability mass function for binomial dist     
import matplotlib.pyplot as plt                    # Makes graphs for visualisation 

# Generate random numbers in the specified range with a step value of 0.05 - Set 1
x = np.arange (400, 600, 0.5)                      # Generate random numbers within 400 to 500 with an increment of 0.5

# Average number of visits per day
mu = 500                                           # Average value to be used in the Poisson Distribution

# Plot the poisson distribution curve
plt.plot(x, poisson.pmf(x, mu))                    # Display the poisson distribution curve


# Generate random numbers in the specified range with a step value of 0.05 - Set 2
x = np.arange (400, 1600, 0.5)                     # Generate random numbers within 400 to 1600 with an increment of 0.5

# Average number of visits per day
mu = 800                                           # Average value to be used in the Poisson Distribution

# Plot the poisson distribution curve
plt.plot(x, poisson.pmf(x, mu))                    # Display the poisson distribution curve

# Generate random numbers in the specified range with a step value of 0.05 - Set 3
x = np.arange (400, 1600, 0.5)                     # Generate random numbers within 400 to 1600 with an increment of 0.5

# Average number of visits per day
mu = 1200                                          # Average value to be used in the Poisson Distribution

# Plot the poisson distribution curve
plt.plot(x, poisson.pmf(x, mu))                    # Display the poisson distribution curve

# Generate random numbers in the specified range with a step value of 0.05 - Set 4
x = np.arange (-400, 1600, 0.5)                    # Generate random numbers within -400 to 1600 with an increment of 0.5

# Average number of visits per day
mu = 200                                           # Average value to be used in the Poisson Distribution

# Plot the poisson distribution curve
plt.plot(x, poisson.pmf(x, mu))                    # Display the poisson distribution curve

# Generate random numbers in the specified range with a step value of 0.05 - Set 5
x = np.arange (400, 500, 0.5)                      # Generate random numbers within 400 to 500 with an increment of 0.5

# Average number of visits per day
mu = 450                                           # Average value to be used in the Poisson Distribution

# Plot the poisson distribution curve
plt.plot(x, poisson.pmf(x, mu))                    # Display the poisson distribution curve

## End of Practice ##