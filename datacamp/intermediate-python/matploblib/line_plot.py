"""
With matplotlib, you can create a bunch of different plots in Python. The most basic plot is the line plot. A general recipe is given here.

import matplotlib.pyplot as plt

plt.plot(x,y)
plt.show()

In the video, you already saw how much the world population has grown over the past years.
Will it continue to do so? The world bank has estimates of the world population for the years 1950 up to 2100. 
The years are loaded in your workspace as a list called year, and the corresponding populations as a list called pop.

This course touches on a lot of concepts you may have forgotten, so if you ever need a quick refresher, download the Python for data science Cheat Sheet and keep it handy!

Now that you've built your first line plot, let's start working on the data that professor Hans Rosling used to build his beautiful bubble chart. It was collected in 2007. Two lists are available for you:

life_exp which contains the life expectancy for each country and
gdp_cap, which contains the GDP per capita (i.e. per person) for each country expressed in US Dollars.
GDP stands for Gross Domestic Product. It basically represents the size of the economy of a country. Divide this by the population and you get the GDP per capita.

matplotlib.pyplot is already imported as plt, so you can get started straight away.

----------------
Instructions

print() the last item from both the year and the pop list to see what the predicted population for the year 2100 is. 
Use two print() functions.
Before you can start, you should import matplotlib.pyplot as plt. 
pyplot is a sub-package of matplotlib, hence the dot.
Use plt.plot() to build a line plot. year should be mapped on the horizontal axis, pop on the vertical axis. 
Don't forget to finish off with the plt.show() function to actually display the plot

Print the last item from both the list gdp_cap, and the list life_exp; it is information about Zimbabwe.
Build a line chart, with gdp_cap on the x-axis, and life_exp on the y-axis. Does it make sense to plot this data on a line plot?
Don't forget to finish off with a plt.show() command, to actually display the plot.

"""

# Print the last item from year and pop
print(year[-1])
print(pop[-1])


# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt


# Make a line plot: year on the x-axis, pop on the y-axis
plt.plot(year, pop)

# Display the plot with plt.show()
plt.show()

# Print the last item of gdp_cap and life_exp


# Make a line plot, gdp_cap on the x-axis, life_exp on the y-axis


# Display the plot
