import sys

# check if arguments are given
if len(sys.argv) < 3:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
else:
    a = int(sys.argv[1])
    b = int(sys.argv[2])

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
