# -*- coding: utf-8 -*-
"""
Udemy Course - Moments : 30-Aug-2019
"""
# Moments - Quantitative measures of the shape of a probability density function
# First moment of a dataset  : Mean
# Second moment of a dataset : Variance
# Third moment of a dataset  : Skew - How lopsided is the distribution
# Skew     - Distribution with a longer tail on the left will be skewed left and has a negative skewness
# Skew     - Distribution with a longer tail on the right will be skewed right and has a positive skewness
# Fourth moment of a dataset : Kurtosis - How thick is the tail and how sharp is the peak compared to a normal distribution
# Kurtosis - Higher peak value has a higher kurtosis, measures how peaked is the data

# Moments Examples
# Import required libraries
import numpy as np                                 # Makes calculation of Mean, Median, Mode, Standard Deviation, Variance
import matplotlib.pyplot as plt                    # Makes graphs for visualisation

# Generate random numbers with normal distribution - Set 1
vals = np.random.normal(0, 0.5, 10000)             # Generate random numbers with normal distribution; mu = 0, sigma = 0.5

# Segment the income data into 50 buckets, and plot it as a histogram
plt.hist(vals, 50)                                 # Segments the data into 50 buckets
plt.show()                                         # Display the histogram    

# First moment of a dataset  : Mean
np.mean(vals)                                      # Gives the first moment - Mean

# Second moment of a dataset : Variance
np.var(vals)                                       # Gives the second moment - Variance

# Third moment of a dataset  : Skew
# Import required libraries
import scipy.stats as sp                           # Makes calculations of Skewness and Kurtosis
sp.skew(vals)                                      # Gives the third moment - Skew
# As the data is centered around Zero, it will also be Zero

# Fourth moment of a dataset : Kurtosis
sp.kurtosis(vals)                                  # Gives the fourth moment - Kurtosis
# As it describes the shape of the tail, it will be Zero for a normal distribution

# Generate random numbers with normal distribution - Set 2
vals = np.random.normal(10, 2.5, 10000)            # Generate random numbers with normal distribution; mu = 10, sigma = 2.5

# Segment the income data into 50 buckets, and plot it as a histogram
plt.hist(vals, 50)                                 # Segments the data into 50 buckets
plt.show()                                         # Display the histogram    

# First moment of a dataset  : Mean
np.mean(vals)                                      # Gives the first moment - Mean

# Second moment of a dataset : Variance
np.var(vals)                                       # Gives the second moment - Variance

# Third moment of a dataset  : Skew
# Import required libraries
import scipy.stats as sp                           # Makes calculations of Skewness and Kurtosis
sp.skew(vals)                                      # Gives the third moment - Skew
# As the data is centered around Zero, it will also be Zero

# Fourth moment of a dataset : Kurtosis
sp.kurtosis(vals)                                  # Gives the fourth moment - Kurtosis
# As it describes the shape of the tail, it will be Zero for a normal distribution

# Generate random numbers with uniform distribution - Set 3
vals = np.random.uniform(-10.0, 10.0, 10000)       # Generate random numbers with uniform distribution

# Segment the income data into 50 buckets, and plot it as a histogram
plt.hist(vals, 50)                                 # Segments the data into 50 buckets
plt.show()                                         # Display the histogram

# First moment of a dataset  : Mean
np.mean(vals)                                      # Gives the first moment - Mean

# Second moment of a dataset : Variance
np.var(vals)                                       # Gives the second moment - Variance

# Third moment of a dataset  : Skew
# Import required libraries
import scipy.stats as sp                           # Makes calculations of Skewness and Kurtosis
sp.skew(vals)                                      # Gives the third moment - Skew

# Fourth moment of a dataset : Kurtosis
sp.kurtosis(vals)                                  # Gives the fourth moment - Kurtosis

# Generate random numbers in the specified range with a step value of 0.001 - Set 4
vals = np.arange(-4, 14, 0.001)                    # Generate random numbers within -3 to + 3 with an increment of 0.001

# Plot the normal distribution curve
# Import required libraries
from scipy.stats import norm                       # Provides pdf function to create probability density function for normal distribution
import matplotlib.pyplot as plt                    # Makes graphs for visualisation

plt.plot(vals, norm.pdf(vals))                     # Display the normal distribution curve

# First moment of a dataset  : Mean
np.mean(vals)                                      # Gives the first moment - Mean

# Second moment of a dataset : Variance
np.var(vals)                                       # Gives the second moment - Variance

# Third moment of a dataset  : Skew
# Import required libraries
import scipy.stats as sp                           # Makes calculations of Skewness and Kurtosis
sp.skew(vals)                                      # Gives the third moment - Skew

# Fourth moment of a dataset : Kurtosis
sp.kurtosis(vals)                                  # Gives the fourth moment - Kurtosis

## End of Practice ##