class Student:
    school = "ABC School"   # class variable

    def __init__(self, name):
        self.name = name    # instance variable

s1 = Student("Rahul")
s2 = Student("Priya")

# Change class variable
Student.school = "XYZ School"

# Change instance variable
s1.name = "Amit"

print(s1.name, s1.school)
print(s2.name, s2.school)
