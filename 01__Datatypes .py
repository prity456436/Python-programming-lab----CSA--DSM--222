# Program to demonstrate built-in data types,
# and display their type and memory location

# Different data types
a = 10          # Integer
b = 3.5         # Float
c = "Hello"     # String
d = [1, 2, 3]   # List
e = (4, 5)      # Tuple
f = {6, 7}      # Set
g = {"x": 1}    # Dictionary
h = True        # Boolean
i = None        # NoneType

# Store all variables in a list
data = [a, b, c, d, e, f, g, h, i]

# Loop through each value and print details
for x in data:
    print("Value:", x)          # Prints the value
    print("Type:", type(x))     # Prints data type
    print("ID:", id(x))         # Prints memory location
    print("-" * 30)             # Separator for clarity