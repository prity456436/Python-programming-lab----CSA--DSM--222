#Demonstrate tuple packing and unpacking with nested tuples.
# Tuple Packing (including nested tuple)
data = ("Alice", 20, (85, 90, 95))   # name, age, (marks)

# Tuple Unpacking (nested unpacking)
name, age, (m1, m2, m3) = data

# Display values
print("Name:", name)
print("Age:", age)
print("Marks:", m1, m2, m3)