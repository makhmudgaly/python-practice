"""
In the previous exercise, you identified optional arguments by viewing the documentation with help(). 
You'll now apply this to change the behavior of the sorted() function.

Have a look at the documentation of sorted() by typing help(sorted) in the IPython Shell.

You'll see that sorted() takes three arguments: iterable, key, and reverse.

key=None means that if you don't specify the key argument, it will be None. reverse=False means that if you don't specify the reverse argument, it will be False, by default.

In this exercise, you'll only have to specify iterable and reverse, not key. 
The first input you pass to sorted() will be matched to the iterable argument, but what about the second input?
 To tell Python you want to specify reverse without changing anything about key, you can use = to assign it a new value:

sorted(____, reverse=____)
Two lists have been created for you. Can you paste them together and sort them in descending order?

Note: For now, we can understand an iterable as being any collection of objects, e.g., a List.
----------------------
Instructions

Use + to merge the contents of first and second into a new list: full.
Call sorted() on full and specify the reverse argument to be True. Save the sorted list as full_sorted.
Finish off by printing out full_sorted.
"""

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse=True)

# Print out full_sorted
print(full_sorted)