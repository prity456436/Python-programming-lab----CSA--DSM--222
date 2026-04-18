# Create a dictionary of student names and marks. Find topper, average, and sort by marks.
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90
}

# Topper
topper = max(students, key=students.get)

# Average
average = sum(students.values()) / len(students)

# Sort by marks
sorted_students = sorted(students.items(), key=lambda x: x[1])

# Output
print("Topper:", topper, "-", students[topper])
print("Average Marks:", average)
print("Sorted by Marks:", sorted_students)