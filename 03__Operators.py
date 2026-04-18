#Write a program to demonstrate all operators (arithmetic, 
#relational, logical, bitwise, assignment).

a = 10
b = 5
print('a =',10,'b =',5)
# -------------------------------
# Arithmetic Operators
# -------------------------------
print("Arithmetic Operators:")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)
print("a ** b =", a ** b)
print("a // b =", a // b)
print("-" * 40)

# -------------------------------
# Relational Operators
# -------------------------------
print("Relational Operators:")
print("a > b =", a > b)
print("a < b =", a < b)
print("a == b =", a == b)
print("a != b =", a != b)
print("a >= b =", a >= b)
print("a <= b =", a <= b)
print("-" * 40)

# -------------------------------
# Logical Operators
# -------------------------------
print("Logical Operators:")
print("(a > 5 and b < 10) =", (a > 5 and b < 10))
print("(a > 5 or b > 10) =", (a > 5 or b > 10))
print("not(a > b) =", not(a > b))
print("-" * 40)

# -------------------------------
# Bitwise Operators
# -------------------------------
print("Bitwise Operators:")
print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("~a =", ~a)
print("a << 1 =", a << 1)
print("a >> 1 =", a >> 1)
print("-" * 40)

# -------------------------------
# Assignment Operators
# -------------------------------
print("Assignment Operators:")
c = a
print("c =", c)

c += b
print("c += b →", c)

c -= b
print("c -= b →", c)

c *= b
print("c *= b →", c)

c /= b
print("c /= b →", c)

c %= b
print("c %= b →", c)

c **= b
print("c **= b →", c)

c //= b
print("c //= b →", c)