# factorial_22.py

def factorial(n):
    """Return factorial of a number"""
    if n < 0:
        return "Not defined for negative numbers"
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def is_prime(n):
    """Check whether a number is prime"""
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
