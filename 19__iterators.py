# 19.Write a program to demonstrate use of iterators.

# create a list
numbers = [10, 20, 30, 40]

# create iterator from list
it = iter(numbers)

# access elements using iterator
print(next(it))  # first element
print(next(it))  # second element
print(next(it))  # third element
print(next(it))  # fourth element
