#Given a mixed list, separate elements based on their datatype.

data = [10, 3.5, "Hi", True, [1,2], (3,4)]

ints, floats, strings, bools = [], [], [], []

for x in data:
    if type(x) == int: ints.append(x)
    elif type(x) == float: floats.append(x)
    elif type(x) == str: strings.append(x)
    elif type(x) == bool: bools.append(x)

print("Integers:", ints)
print("Floats:", floats)
print("Strings:", strings)
print("Booleans:", bools)