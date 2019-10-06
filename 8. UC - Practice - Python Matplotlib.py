# -*- coding: utf-8 -*-
"""
Udemy Course - Matplotlib : 30-Aug-2019
"""
# Matplotlib - Used to create graphs and visualize different types of data in different ways
# Matplotlib - Chooses different colors automatically for different plots

# Import required libraries
from scipy.stats import norm                       # Provides pdf function to create probability density function for normal distribution
import numpy as np                                 # Makes calculation of Mean, Median, Mode, Standard Deviation, Variance
import matplotlib.pyplot as plt                    # Makes graphs for visualisation

# Draw a line graph
# Generate random numbers in the specified range with a step value of 0.001 - Set 1
x = np.arange(-3, 3, 0.001)                        # Generate random numbers within -3 to + 3 with an increment of 0.001

# Plot the normal distribution curve
plt.plot(x, norm.pdf(x))                           # Display the normal distribution curve
plt.show()                                         # Display the plot 

# Multiple plots on one graph - Set 1
plt.plot(x, norm.pdf(x))                           # Display the first normal distribution curve
plt.plot(x, norm.pdf(x, 1.0, 0.5))                 # Display the second normal distribution curve
plt.show()                                         # Display the plot

# Multiple plots on one graph - Set 2
plt.plot(x, norm.pdf(x))                           # Display the first normal distribution curve
plt.plot(x, norm.pdf(x, 1.0, 0.5))                 # Display the second normal distribution curve
plt.plot(x, norm.pdf(x, 1.0, 0.25))                # Display the third normal distribution curve
plt.show()                                         # Display the plot

# Saving the plots on a file - Set 1
plt.plot(x, norm.pdf(x))                           # Display the first normal distribution curve
plt.plot(x, norm.pdf(x, 1.0, 0.5))                 # Display the second normal distribution curve
plt.savefig("C:/Abhinav/Study Material/Data Science/Udemy/Practice/firstplot.png",format='png')   # Save the plots on a .png file
plt.savefig("C:/Abhinav/Study Material/Data Science/Udemy/Practice/firstplot.jpg",format='jpg')   # Save the plots on a .jpg file

# Saving the plots on a file - Set 2
plt.plot(x, norm.pdf(x))                           # Display the first normal distribution curve
plt.plot(x, norm.pdf(x, 1.0, 0.5))                 # Display the second normal distribution curve
plt.plot(x, norm.pdf(x, 1.0, 0.25))                # Display the third normal distribution curve
plt.savefig("C:/Abhinav/Study Material/Data Science/Udemy/Practice/secondplot.png",format='png')   # Save the plots on a .png file
plt.savefig("C:/Abhinav/Study Material/Data Science/Udemy/Practice/secondplot.jpg",format='jpg')   # Save the plots on a .jpg file

# Adjust the axes - Set 1
axes = plt.axes()                                  # Mapping the axes
axes.set_xlim([-5, 5])                             # Setting the limit for x axis 
axes.set_ylim([0, 1.0])                            # Setting the limit for y axis
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])                  # Setting the parameters for ticks on the x axis
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])   # Setting the parameters for ticks on the y axis
plt.plot(x, norm.pdf(x))                           # Display the first normal distribution curve
plt.plot(x, norm.pdf(x, 1.0, 0.5))                 # Display the second normal distribution curve
plt.show()                                         # Display the plot

# Adjust the axes - Set 2
axes = plt.axes()                                  # Mapping the axes
axes.set_xlim([-5, 8])                             # Setting the limit for x axis - Extends the axis
axes.set_ylim([0, 1.0])                            # Setting the limit for y axis
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])                  # Setting the parameters for ticks on the x axis
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])   # Setting the parameters for ticks on the y axis
plt.plot(x, norm.pdf(x))                           # Display the first normal distribution curve
plt.plot(x, norm.pdf(x, 1.0, 0.5))                 # Display the second normal distribution curve
plt.show()                                         # Display the plot

# Adjust the axes - Set 3
axes = plt.axes()                                  # Mapping the axes
axes.set_xlim([-5, 8])                             # Setting the limit for x axis - Extends the axis
axes.set_ylim([0, 1.0])                            # Setting the limit for y axis
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 7])         # Setting the parameters for ticks on the x axis - Extends the ticks
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])   # Setting the parameters for ticks on the y axis
plt.plot(x, norm.pdf(x))                           # Display the first normal distribution curve
plt.plot(x, norm.pdf(x, 1.0, 0.5))                 # Display the second normal distribution curve
plt.show()                                         # Display the plot

# Adjust the axes - Set 4
axes = plt.axes()                                  # Mapping the axes
axes.set_xlim([-5, 2])                             # Setting the limit for x axis - Leads to truncation
axes.set_ylim([0, 1.0])                            # Setting the limit for y axis
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2])     # Setting the parameters for ticks on the x axis - Leads to truncation
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])   # Setting the parameters for ticks on the y axis
plt.plot(x, norm.pdf(x))                           # Display the first normal distribution curve
plt.plot(x, norm.pdf(x, 1.0, 0.5))                 # Display the second normal distribution curve
plt.show()                                         # Display the plot

# Adjust the axes - Set 5
axes = plt.axes()                                  # Mapping the axes
axes.set_xlim([-5, 5])                             # Setting the limit for x axis
axes.set_ylim([0, 0.5])                            # Setting the limit for y axis - Leads to truncation
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5 ])         # Setting the parameters for ticks on the x axis
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5])                    # Setting the parameters for ticks on the y axis - Leads to truncation
plt.plot(x, norm.pdf(x))                           # Display the first normal distribution curve
plt.plot(x, norm.pdf(x, 1.0, 0.5))                 # Display the second normal distribution curve
plt.show()                                         # Display the plot

# Adding the grid
axes = plt.axes()                                  # Mapping the axes
axes.set_xlim([-5, 5])                             # Setting the limit for x axis 
axes.set_ylim([0, 1.0])                            # Setting the limit for y axis
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])                  # Setting the parameters for ticks on the x axis
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])   # Setting the parameters for ticks on the y axis
axes.grid()                                        # Display the gridlines
plt.plot(x, norm.pdf(x))                           # Display the first normal distribution curve
plt.plot(x, norm.pdf(x, 1.0, 0.5))                 # Display the second normal distribution curve
plt.show()                                         # Display the plot

# Change line type and colors of the plot - Set 1
axes = plt.axes()                                  # Mapping the axes
axes.set_xlim([-5, 5])                             # Setting the limit for x axis 
axes.set_ylim([0, 1.0])                            # Setting the limit for y axis
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])                  # Setting the parameters for ticks on the x axis
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])   # Setting the parameters for ticks on the y axis
axes.grid()                                        # Display the gridlines
plt.plot(x, norm.pdf(x), 'b-')                     # Display the first normal distribution curve with solid line in blue color
plt.plot(x, norm.pdf(x, 1.0, 0.5), 'r:')           # Display the second normal distribution curve with dotted line in red color
plt.show()                                         # Display the plot 

# Change line type and colors of the plot - Set 2
axes = plt.axes()                                  # Mapping the axes
axes.set_xlim([-5, 5])                             # Setting the limit for x axis 
axes.set_ylim([0, 1.0])                            # Setting the limit for y axis
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])                  # Setting the parameters for ticks on the x axis
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])   # Setting the parameters for ticks on the y axis
axes.grid()                                        # Display the gridlines
plt.plot(x, norm.pdf(x), 'b-')                     # Display the first normal distribution curve with solid line in blue color
plt.plot(x, norm.pdf(x, 1.0, 0.5), 'g--')          # Display the second normal distribution curve with double dotted line in green color
plt.show()                                         # Display the plot 

# Change line type and colors of the plot - Set 3
axes = plt.axes()                                  # Mapping the axes
axes.set_xlim([-5, 5])                             # Setting the limit for x axis 
axes.set_ylim([0, 1.0])                            # Setting the limit for y axis
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])                  # Setting the parameters for ticks on the x axis
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])   # Setting the parameters for ticks on the y axis
axes.grid()                                        # Display the gridlines
plt.plot(x, norm.pdf(x), 'b-')                     # Display the first normal distribution curve with solid line in blue color
plt.plot(x, norm.pdf(x, 1.0, 0.5), 'g-.')          # Display the second normal distribution curve with slash and dotted line in green color
plt.show()                                         # Display the plot

# Change line type and colors of the plot - Set 4
axes = plt.axes()                                  # Mapping the axes
axes.set_xlim([-5, 5])                             # Setting the limit for x axis 
axes.set_ylim([0, 1.0])                            # Setting the limit for y axis
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])                  # Setting the parameters for ticks on the x axis
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])   # Setting the parameters for ticks on the y axis
axes.grid()                                        # Display the gridlines
plt.plot(x, norm.pdf(x), 'b--')                    # Display the first normal distribution curve with double dotted line in blue color
plt.plot(x, norm.pdf(x, 1.0, 0.5), 'g-.')          # Display the second normal distribution curve with slash and dotted line in green color
plt.show()                                         # Display the plot

# Labelling axes and Adding Legends - Position : Top Right
axes = plt.axes()                                  # Mapping the axes
axes.set_xlim([-5, 5])                             # Setting the limit for x axis 
axes.set_ylim([0, 1.0])                            # Setting the limit for y axis
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])                  # Setting the parameters for ticks on the x axis
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])   # Setting the parameters for ticks on the y axis
axes.grid()                                        # Display the gridlines
plt.xlabel('X-Axis')                               # Display the label for X-Axis
plt.ylabel('Y-Axis')                               # Display the label for X-Axis
plt.plot(x, norm.pdf(x), 'b--')                    # Display the first normal distribution curve with double dotted line in blue color
plt.plot(x, norm.pdf(x, 1.0, 0.5), 'g-.')          # Display the second normal distribution curve with slash and dotted line in green color
plt.legend(['Blue','Green'], loc = 0)              # Display the legend for plot type, 0 is for Top Right
plt.show()                                         # Display the plot

# Labelling axes and Adding Legends - Position : Top Left
axes = plt.axes()                                  # Mapping the axes
axes.set_xlim([-5, 5])                             # Setting the limit for x axis 
axes.set_ylim([0, 1.0])                            # Setting the limit for y axis
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])                  # Setting the parameters for ticks on the x axis
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])   # Setting the parameters for ticks on the y axis
axes.grid()                                        # Display the gridlines
plt.xlabel('X-Axis')                               # Display the label for X-Axis
plt.ylabel('Y-Axis')                               # Display the label for X-Axis
plt.plot(x, norm.pdf(x), 'b--')                    # Display the first normal distribution curve with double dotted line in blue color
plt.plot(x, norm.pdf(x, 1.0, 0.5), 'g-.')          # Display the second normal distribution curve with slash and dotted line in green color
plt.legend(['Blue','Green'], loc = 2)              # Display the legend for plot type, 2 is for Top Left
plt.show()                                         # Display the plot

# Labelling axes and Adding Legends - Position : Bottom Left
axes = plt.axes()                                  # Mapping the axes
axes.set_xlim([-5, 5])                             # Setting the limit for x axis 
axes.set_ylim([0, 1.0])                            # Setting the limit for y axis
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])                  # Setting the parameters for ticks on the x axis
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])   # Setting the parameters for ticks on the y axis
axes.grid()                                        # Display the gridlines
plt.xlabel('X-Axis')                               # Display the label for X-Axis
plt.ylabel('Y-Axis')                               # Display the label for X-Axis
plt.plot(x, norm.pdf(x), 'b--')                    # Display the first normal distribution curve with double dotted line in blue color
plt.plot(x, norm.pdf(x, 1.0, 0.5), 'g-.')          # Display the second normal distribution curve with slash and dotted line in green color
plt.legend(['Blue','Green'], loc = 3)              # Display the legend for plot type, 3 is for Bottom Left
plt.show()                                         # Display the plot

# Labelling axes and Adding Legends - Position : Bottom Right
axes = plt.axes()                                  # Mapping the axes
axes.set_xlim([-5, 5])                             # Setting the limit for x axis 
axes.set_ylim([0, 1.0])                            # Setting the limit for y axis
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])                  # Setting the parameters for ticks on the x axis
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])   # Setting the parameters for ticks on the y axis
axes.grid()                                        # Display the gridlines
plt.xlabel('X-Axis')                               # Display the label for X-Axis
plt.ylabel('Y-Axis')                               # Display the label for X-Axis
plt.plot(x, norm.pdf(x), 'b--')                    # Display the first normal distribution curve with double dotted line in blue color
plt.plot(x, norm.pdf(x, 1.0, 0.5), 'g-.')          # Display the second normal distribution curve with slash and dotted line in green color
plt.legend(['Blue','Green'], loc = 4)              # Display the legend for plot type, 4 is for Bottom Right
plt.show()                                         # Display the plot

# Labelling axes and Adding Legends - Position : Middle Right
axes = plt.axes()                                  # Mapping the axes
axes.set_xlim([-5, 5])                             # Setting the limit for x axis 
axes.set_ylim([0, 1.0])                            # Setting the limit for y axis
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])                  # Setting the parameters for ticks on the x axis
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])   # Setting the parameters for ticks on the y axis
axes.grid()                                        # Display the gridlines
plt.xlabel('X-Axis')                               # Display the label for X-Axis
plt.ylabel('Y-Axis')                               # Display the label for X-Axis
plt.plot(x, norm.pdf(x), 'b--')                    # Display the first normal distribution curve with double dotted line in blue color
plt.plot(x, norm.pdf(x, 1.0, 0.5), 'g-.')          # Display the second normal distribution curve with slash and dotted line in green color
plt.legend(['Blue','Green'], loc = 5)              # Display the legend for plot type, 5 is for Middle Right
plt.show()                                         # Display the plot

# Labelling axes and Adding Legends - Position : Middle Left
axes = plt.axes()                                  # Mapping the axes
axes.set_xlim([-5, 5])                             # Setting the limit for x axis 
axes.set_ylim([0, 1.0])                            # Setting the limit for y axis
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])                  # Setting the parameters for ticks on the x axis
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])   # Setting the parameters for ticks on the y axis
axes.grid()                                        # Display the gridlines
plt.xlabel('X-Axis')                               # Display the label for X-Axis
plt.ylabel('Y-Axis')                               # Display the label for X-Axis
plt.plot(x, norm.pdf(x), 'b--')                    # Display the first normal distribution curve with double dotted line in blue color
plt.plot(x, norm.pdf(x, 1.0, 0.5), 'g-.')          # Display the second normal distribution curve with slash and dotted line in green color
plt.legend(['Blue','Green'], loc = 6)              # Display the legend for plot type, 6 is for Middle Left
plt.show()                                         # Display the plot

# Labelling axes and Adding Legends - Position : Middle Bottom
axes = plt.axes()                                  # Mapping the axes
axes.set_xlim([-5, 5])                             # Setting the limit for x axis 
axes.set_ylim([0, 1.0])                            # Setting the limit for y axis
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])                  # Setting the parameters for ticks on the x axis
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])   # Setting the parameters for ticks on the y axis
axes.grid()                                        # Display the gridlines
plt.xlabel('X-Axis')                               # Display the label for X-Axis
plt.ylabel('Y-Axis')                               # Display the label for X-Axis
plt.plot(x, norm.pdf(x), 'b--')                    # Display the first normal distribution curve with double dotted line in blue color
plt.plot(x, norm.pdf(x, 1.0, 0.5), 'g-.')          # Display the second normal distribution curve with slash and dotted line in green color
plt.legend(['Blue','Green'], loc = 8)              # Display the legend for plot type, 8 is for Middle Bottom
plt.show()                                         # Display the plot

# Labelling axes and Adding Legends - Position : Top Middle
axes = plt.axes()                                  # Mapping the axes
axes.set_xlim([-5, 5])                             # Setting the limit for x axis 
axes.set_ylim([0, 1.0])                            # Setting the limit for y axis
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])                  # Setting the parameters for ticks on the x axis
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])   # Setting the parameters for ticks on the y axis
axes.grid()                                        # Display the gridlines
plt.xlabel('X-Axis')                               # Display the label for X-Axis
plt.ylabel('Y-Axis')                               # Display the label for X-Axis
plt.plot(x, norm.pdf(x), 'b--')                    # Display the first normal distribution curve with double dotted line in blue color
plt.plot(x, norm.pdf(x, 1.0, 0.5), 'g-.')          # Display the second normal distribution curve with slash and dotted line in green color
plt.legend(['Blue','Green'], loc = 9)              # Display the legend for plot type, 9 is for Top Middle
plt.show()                                         # Display the plot

# Labelling axes and Adding Legends - Position : Middle Middle
axes = plt.axes()                                  # Mapping the axes
axes.set_xlim([-5, 5])                             # Setting the limit for x axis 
axes.set_ylim([0, 1.0])                            # Setting the limit for y axis
axes.set_xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])                  # Setting the parameters for ticks on the x axis
axes.set_yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])   # Setting the parameters for ticks on the y axis
axes.grid()                                        # Display the gridlines
plt.xlabel('X-Axis')                               # Display the label for X-Axis
plt.ylabel('Y-Axis')                               # Display the label for X-Axis
plt.plot(x, norm.pdf(x), 'b--')                    # Display the first normal distribution curve with double dotted line in blue color
plt.plot(x, norm.pdf(x, 1.0, 0.5), 'g-.')          # Display the second normal distribution curve with slash and dotted line in green color
plt.legend(['Blue','Green'], loc = 10)             # Display the legend for plot types 10 is for Middle Middle
plt.show()                                         # Display the plot

# XKCD Style - Try Again
plt.xkcd()                                         # Function to put matplotlib in XKCD mode
fig = plt.figure()                                 # Function to plot the figure
ax = fig.add_subplot(1, 1, 1)                      # Adding the subplot to the figure
ax.spines['right'].set_color('none')               # Setting the position and color
ax.spines['top'].set_color('none')                 # Setting the position and color
plt.xticks([])                                     # Setting the parameters for ticks on the x axis
plt.yticks([])                                     # Setting the parameters for ticks on the x axis
ax.set_ylim([-30, 10])                             # Setting the limit for y axis

# Creating the data to be displayed
data = np.ones(100)                                # Creating the data to be displayed
data[70:] -= np.arange(30)                         # Creating the data to be displayed

# Preparing the text to be displayed/annotated
# plt.annotate('This is my\n first\n XKCD Plot', xy(70, 1), arrowprops=dict(arrowstyle='->'), xytext=(-15,10))

plt.plot(data)                                     # Plotting the graph with the data

plt.xlabel('Time')                                 # Display the label for X-Axis
plt.xlabel('My Practice')                          # Display the label for Y-Axis

# Pie Chart- Set 1
plt.rcdefaults()                                   # Return to default as we had set the plotting to XKCD mode in the previous example
values = [12, 55, 4, 32, 14]                       # Setting the percentage values to be shown on the pie chart
colors = ['r', 'g', 'b', 'c', 'm']                 # Setting the color values to be shown on the pie chart
explode = [0, 0, 0.2, 0, 0]                        # Setting the percentage value to explode and come out
labels = ['India', 'United States', 'Russia', 'China', 'Europe']      # Setting the label values to be shown on the pie chart
plt.pie(values, colors = colors, labels = labels, explode = explode)  # Creating the pie chart
plt.title('Pie Chart')                             # Setting the pie chart title to be shown on the pie chart
plt.show()                                         # Display the plot

# Pie Chart- Set 2
plt.rcdefaults()                                   # Return to default as we had set the plotting to XKCD mode in the previous example
values = [12, 55, 4, 32, 14]                       # Setting the percentage values to be shown on the pie chart
colors = ['r', 'g', 'b', 'c', 'm']                 # Setting the color values to be shown on the pie chart
explode = [0.5, 0, 0.2, 0, 0]                      # Setting the percentage value to explode and come out
labels = ['India', 'United States', 'Russia', 'China', 'Europe']      # Setting the label values to be shown on the pie chart
plt.pie(values, colors = colors, labels = labels, explode = explode)  # Creating the pie chart
plt.title('Pie Chart')                             # Setting the pie chart title to be shown on the pie chart
plt.show()                                         # Display the plot

# Bar Chart - Set 1
values = [12, 55, 4, 32, 14]                       # Setting the values to be shown on the bar chart
colors = ['r', 'g', 'b', 'c', 'm']                 # Setting the color values to be shown on the bar chart
plt.bar(range(0, 5), values, color = colors) # Creating the bar chart
plt.show()                                         # Display the plot

# Bar Chart - Set 2
values = [12, 55, 4, 32, 14]                       # Setting the values to be shown on the bar chart
colors = ['r', 'g', 'b', 'c', 'm']                 # Setting the color values to be shown on the bar chart
plt.bar(range(0, 5), values, color = colors)       # Creating the bar chart
plt.title('Bar Chart')                             # Setting the bar chart title to be shown on the bar chart
plt.show()                                         # Display the plot

# Scatter Plot - Set 1
X = np.random.randn(500)                           # Generate random distribution of numbers to be plotted
Y = np.random.randn(500)                           # Generate random distribution of numbers to be plotted
plt.scatter(X,Y)                                   # Creating the scatter plot
plt.show()                                         # Display the plot

# Scatter Plot - Set 2
X = np.random.randn(750)                           # Generate random distribution of numbers to be plotted
Y = np.random.randn(750)                           # Generate random distribution of numbers to be plotted
plt.scatter(X,Y)                                   # Creating the scatter plot
plt.xlabel('X-Axis')                               # Display the label for X-Axis
plt.ylabel('Y-Axis')                               # Display the label for X-Axis
plt.title('Scatter Plot')                          # Setting the scatter plot title to be shown on the scatter plot
plt.show()                                         # Display the plot

# Histogram - Set 1
incomes = np.random.normal(27000, 15000, 10000)    # Generate random numbers with normal distribution; mu = 27000, sigma = 15000
plt.hist(incomes, 50)                              # Segments the data into 50 buckets
plt.xlabel('X-Axis')                               # Display the label for X-Axis
plt.ylabel('Y-Axis')                               # Display the label for X-Axis
plt.title('Histogram')                             # Setting the histogram title to be shown on the histogram
plt.show()                                         # Display the histogram    

# Histogram - Set 2
incomes = np.random.normal(57000, 25000, 50000)    # Generate random numbers with normal distribution; mu = 27000, sigma = 15000
plt.hist(incomes, 50)                              # Segments the data into 50 buckets
plt.xlabel('X-Axis')                               # Display the label for X-Axis
plt.ylabel('Y-Axis')                               # Display the label for X-Axis
plt.title('Histogram')                             # Setting the histogram title to be shown on the histogram
plt.show()                                         # Display the histogram    

# Box and Whisker Plot
# Box and Whisker Plot - Used for visualizing the spread and skewness of the data
# Box represents the interquartile range and contains half of the data
# Middle line represents the Median of the data and the box represents the bounds of the first and third quartile
# Dotted line (Whiskers) indicate the range of the data except for the outliers which are plotted outside the whiskers
# Outliers are 1.5 times more than the interquartile range

# Box and Whisker Plot - Set 1
uniformSkewed = np.random.rand(100) * 100 - 40     # Generate random numbers for box plot
high_outliers = np.random.rand(10) * 50 + 100      # Generate random number outliers for box plot 
low_outliers = np.random.rand(10) * 50 - 100       # Generate random number outliers for box plot  
data = np.concatenate((uniformSkewed, high_outliers, low_outliers))   # Prepare the data to be plotted
plt.boxplot(data)                                  # Creating the box plot
plt.xlabel('X-Axis')                               # Display the label for X-Axis
plt.ylabel('Y-Axis')                               # Display the label for X-Axis
plt.title('Box and Whisker')                       # Setting the Box and Whisker title title to be shown on the plot
plt.show()                                         # Display the histogram

# Box and Whisker Plot - Set 2
uniformSkewed = np.random.rand(200) * 100 - 40     # Generate random numbers for box plot
high_outliers = np.random.rand(20) * 50 + 100      # Generate random number outliers for box plot 
low_outliers = np.random.rand(20) * 50 - 100       # Generate random number outliers for box plot  
data = np.concatenate((uniformSkewed, high_outliers, low_outliers))   # Prepare the data to be plotted
plt.boxplot(data)                                  # Creating the box plot
plt.xlabel('X-Axis')                               # Display the label for X-Axis
plt.ylabel('Y-Axis')                               # Display the label for X-Axis
plt.title('Box and Whisker')                       # Setting the Box and Whisker title title to be shown on the plot
plt.show()                                         # Display the histogram

## End of Practice ##