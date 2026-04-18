# Write a program to count vowels, consonants, digits, and 
# special characters in a string.

s = input("Enter a string: ")

v = c = d = sp = 0   # counters

for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            v += 1
        else:
            c += 1
    elif ch.isdigit():
        d += 1
    else:
        sp += 1

print("Vowels:", v)
print("Consonants:", c)
print("Digits:", d)
print("Special characters:", sp)