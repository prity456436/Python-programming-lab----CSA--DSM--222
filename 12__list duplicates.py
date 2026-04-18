# Remove duplicates from a list while maintaining order.
lst = [10, 5, 8, 10, 5, 3, 8]

result = []
for item in lst:
    if item not in result:
        result.append(item)

print("List after removing duplicates:", result)