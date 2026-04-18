# Check whether a string is a palindrome (with and without slicing).

s = input("Enter a string: ")
rev = ""

for ch in s:
    rev = ch + rev   # reverse string manually

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")