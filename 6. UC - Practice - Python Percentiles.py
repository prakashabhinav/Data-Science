# -*- coding: utf-8 -*-
"""
Udemy Course - Percentiles : 30-Aug-2019
"""
# Percentile - The point in a dataset, at which X% of the values are less than that value. Example : Income Distribution
# Percentiles in a Normal Distribution - Q1, Q2, Q3, Q4
# Percentiles in a Normal Distribution - IQR(Inter Quartile Range) is Q3 - Q1
# Percentiles in a Normal Distribution - IQR holds 50% of the data. 25% on the left of Median and 25% on the right of Median
# Percentiles in a Normal Distribution - Total Range : Q1 - 1.5 * IQR to Q3 + 1.5 * IQR

# Percentiles Examples
# Import required libraries
import numpy as np                                 # Makes calculation of Mean, Median, Mode, Standard Deviation, Variance
import matplotlib.pyplot as plt                    # Makes graphs for visualisation

# Generate random numbers with normal distribution - Set 1
vals = np.random.normal(0, 0.5, 10000)             # Generate random numbers with normal distribution; mu = 0, sigma = 0.5

# Segment the income data into 50 buckets, and plot it as a histogram
plt.hist(vals, 50)                                 # Segments the data into 50 buckets
plt.show()                                         # Display the histogram    

# Calculate Percentile Values using numpy functions
# 50th Percentile
np.percentile(vals, 50)                            # Gives value at 50th percentile which is the Median

# Compute the median
np.median(vals)                                    # Display the median of random values

# 90th Percentile
np.percentile(vals, 90)                            # Gives value at 90th percentile

# 20th Percentile
np.percentile(vals, 20)                            # Gives value at 20th percentile

# 75th Percentile
np.percentile(vals, 75)                            # Gives value at 75th percentile which is the Q3

# 25th Percentile
np.percentile(vals, 25)                            # Gives value at 25th percentile which is the Q1

# Generate random numbers with normal distribution - Set 2
vals = np.random.normal(5, 10, 10000)              # Generate random numbers with normal distribution; mu = 5, sigma = 10

# Segment the income data into 50 buckets, and plot it as a histogram
plt.hist(vals, 50)                                 # Segments the data into 50 buckets
plt.show()                                         # Display the histogram    

# Calculate Percentile Values using numpy functions
# 50th Percentile
np.percentile(vals, 50)                            # Gives value at 50th percentile which is the Median

# Compute the median
np.median(vals)                                    # Display the median of random values

# 90th Percentile
np.percentile(vals, 90)                            # Gives value at 90th percentile

# 20th Percentile
np.percentile(vals, 20)                            # Gives value at 20th percentile

# 75th Percentile
np.percentile(vals, 50)                            # Gives value at 75th percentile which is the Q3

# 25th Percentile
np.percentile(vals, 25)                            # Gives value at 25th percentile which is the Q1

# Generate random numbers with normal distribution - Set 3
vals = np.random.normal(-5, 10, 10000)             # Generate random numbers with normal distribution; mu = -5, sigma = 10

# Segment the income data into 50 buckets, and plot it as a histogram
plt.hist(vals, 50)                                 # Segments the data into 50 buckets
plt.show()                                         # Display the histogram    

# Calculate Percentile Values using numpy functions
# 50th Percentile
np.percentile(vals, 50)                            # Gives value at 50th percentile which is the Median

# Compute the median
np.median(vals)                                    # Display the median of random values

# 90th Percentile
np.percentile(vals, 90)                            # Gives value at 90th percentile

# 20th Percentile
np.percentile(vals, 20)                            # Gives value at 20th percentile

# 75th Percentile
np.percentile(vals, 50)                            # Gives value at 75th percentile which is the Q3

# 25th Percentile
np.percentile(vals, 25)                            # Gives value at 25th percentile which is the Q1

# Generate random numbers with normal distribution - Set 4
vals = np.random.normal(-50, 10, 100)              # Generate random numbers with normal distribution; mu = -50, sigma = 10

# Segment the income data into 50 buckets, and plot it as a histogram
plt.hist(vals, 50)                                 # Segments the data into 50 buckets
plt.show()                                         # Display the histogram    

# Calculate Percentile Values using numpy functions
# 50th Percentile
np.percentile(vals, 50)                            # Gives value at 50th percentile which is the Median

# Compute the median
np.median(vals)                                    # Display the median of random values

# 90th Percentile
np.percentile(vals, 90)                            # Gives value at 90th percentile

# 20th Percentile
np.percentile(vals, 20)                            # Gives value at 20th percentile

# 75th Percentile
np.percentile(vals, 50)                            # Gives value at 75th percentile which is the Q3

# 25th Percentile
np.percentile(vals, 25)                            # Gives value at 25th percentile which is the Q1

## End of Practice ##