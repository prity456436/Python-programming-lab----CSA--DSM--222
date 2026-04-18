#Illustrate mutable and immutable objects with suitable exam- 
#ples.


# LIST (Mutable)
list1 = [1, 2, 3]
list2 = list1   # both refer to same list

list1.append(4)   # modifying list1

print("List (Mutable):")
print("list1 =", list1)   # [1, 2, 3, 4]
print("list2 =", list2)   # [1, 2, 3, 4] (also changed)
print("-" * 30)

# TUPLE (Immutable)
tuple1 = (1, 2, 3)
tuple2 = tuple1   # both refer to same tuple

tuple1 = tuple1 + (4,)   # creates new tuple

print("Tuple (Immutable):")
print("tuple1 =", tuple1)   # (1, 2, 3, 4)
print("tuple2 =", tuple2)   # (1, 2, 3) (unchanged)