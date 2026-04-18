#Write a program to take user input and dynamically determine 
#and convert its datatype.

x = input("Enter a value: ")

# Check for Integer
if x.isdigit():
    x = int(x)
    print("Converted to Integer:", x)

# Check for Float
elif '.' in x:
    try:
        x = float(x)
        print("Converted to Float:", x)
    except:
        print("Invalid Float")

# Check for Boolean
elif x.lower() == "true" or x.lower() == "false":
    x = x.lower() == "true"
    print("Converted to Boolean:", x)

# Otherwise treat as String
else:
    print("It is a String:", x)

# Show final datatype
print("Final Type:", type(x))