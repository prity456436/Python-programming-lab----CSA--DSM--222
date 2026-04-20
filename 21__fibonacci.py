# 21.Write recursive and iterative functions for Fibonacci and compare execution time.

import time

# recursive
def fib_r(n):
    if n<=1:
        return n
    else:
        return fib_r(n-1)+fib_r(n-2)

# iterative
def fib_i(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a

n=30

t=time.time()
print("Rec:", fib_r(n))
print("Time:", time.time()-t)

t=time.time()
print("Itr:", fib_i(n))
print("Time:", time.time()-t)
