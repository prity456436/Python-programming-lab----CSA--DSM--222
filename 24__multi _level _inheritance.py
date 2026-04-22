# Base class (Level 1)
class Person:
    def __init__(self, name):
        self.name = name

    def show_person(self):
        print("Name:", self.name)


# Derived class (Level 2)
class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)   # call parent constructor
        self.salary = salary

    def show_employee(self):
        print("Salary:", self.salary)


# Derived class (Level 3)
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_manager(self):
        print("Department:", self.department)


# 🔹 Using the classes
m = Manager("Rahul", 50000, "IT")

m.show_person()
m.show_employee()
m.show_manager()
