# main.py

import factorial_22

num = int(input("Enter a number: "))

print("Factorial:", factorial_22.factorial(num))

if factorial_22.is_prime(num):
    print("It is a Prime number")
else:
    print("It is NOT a Prime number")
