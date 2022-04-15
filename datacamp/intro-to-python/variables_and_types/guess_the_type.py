"""
Guess the type
To find out the type of a value or a variable that refers to that value, you can use the type() function. Suppose you've defined a variable a, but you forgot the type of this variable. To determine the type of a, simply execute:

```python
type(a)
```
We already went ahead and created three variables: a, b and c. You can use the IPython shell to discover their type. Which of the following options is correct?

"""
a,b,c = 194.87171000000012,"True", False

print(f"type of a is: {type(a)}")
print(f"type of b is: {type(b)}")
print(f"type of c is: {type(c)}")