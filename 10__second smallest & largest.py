# 10.Find second largest and second smallest elements in a list without using built-in functions.
lst = [10, 5, 8, 20, 15, 3]

# Initialize variables
largest = second_largest = -999999
smallest = second_smallest = 999999

# Find largest and smallest
for num in lst:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

# Find second largest and second smallest
for num in lst:
    if num > second_largest and num != largest:
        second_largest = num
    if num < second_smallest and num != smallest:
        second_smallest = num

print("Second Largest:", second_largest)
print("Second Smallest:", second_smallest)