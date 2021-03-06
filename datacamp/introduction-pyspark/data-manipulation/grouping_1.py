"""
Part of what makes aggregating so powerful is the addition of groups. PySpark has a whole class devoted to grouped data frames: pyspark.sql.GroupedData, 
which you saw in the last two exercises.

You've learned how to create a grouped DataFrame by calling the .groupBy() method on a DataFrame with no arguments.

Now you'll see that when you pass the name of one or more columns in your DataFrame to the .groupBy() method, 
the aggregation methods behave like when you use a GROUP BY statement in a SQL query!

Remember, a SparkSession called spark is already in your workspace, along with the Spark DataFrame flights.

Instructions:

Create a DataFrame called by_plane that is grouped by the column tailnum.
Use the .count() method with no arguments to count the number of flights each plane made.
Create a DataFrame called by_origin that is grouped by the column origin.
Find the .avg() of the air_time column to find average duration of flights from PDX and SEA.
"""
