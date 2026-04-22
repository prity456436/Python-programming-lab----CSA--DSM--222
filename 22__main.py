# main.py

import factorial1

num = int(input("Enter a number: "))

print("Factorial:", factorial1.factorial(num))

if factorial1.is_prime(num):
    print("It is a Prime number")
else:
    print("It is NOT a Prime number")
