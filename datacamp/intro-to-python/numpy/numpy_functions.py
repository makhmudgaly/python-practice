"""
You now know how to use numpy functions to get a better feeling for your data. 
It basically comes down to importing numpy and then calling several simple functions on the numpy arrays:

import numpy as np
x = [1, 4, 8, 10, 12]
np.mean(x)
np.median(x)
The baseball data is available as a 2D numpy array with 3 columns (height, weight, age) and 1015 rows. 
The name of this numpy array is np_baseball. After restructuring the data, however, you notice that some height values are abnormally high. 
Follow the instructions and discover which summary statistic is best suited if you're dealing with so-called outliers.

Because the mean and median are so far apart, you decide to complain to the MLB. 
They find the error and send the corrected data over to you. It's again available as a 2D NumPy array np_baseball, with three columns.

The Python script in the editor already includes code to print out informative messages with the different summary statistics. Can you finish the job?
--------------------
Instructions
Create numpy array np_height_in that is equal to first column of np_baseball.
Print out the mean of np_height_in.
Print out the median of np_height_in.

The code to print out the mean height is already included. 
Complete the code for the median height. Replace None with the correct code.
Use np.std() on the first column of np_baseball to calculate stddev. Replace None with the correct code.
Do big players tend to be heavier? Use np.corrcoef() to store the correlation between the first and second column of np_baseball in corr. Replace None with the correct code.
"""

# np_baseball is available

# Import numpy
import numpy as np

# Create np_height_in from np_baseball
np_height_in = np_baseball[:, 0]

# Print out the mean of np_height_in
print(np.mean(np_height_in))

# Print out the median of np_height_in
print(np.median(np_height_in))

# Print mean height (first column)
avg = np.mean(np_baseball[:, 0])
print("Average: " + str(avg))

# Print median height. Replace 'None'
med = np.median(np_baseball[:, 0])
print("Median: " + str(med))

# Print out the standard deviation on height. Replace 'None'
stddev = np.std(np_baseball[:, 0], np_baseball[:, 1])
print("Standard Deviation: " + str(stddev))
