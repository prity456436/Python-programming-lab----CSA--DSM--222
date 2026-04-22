class BankAccount:
    
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        elif amount <= 0:
            print("Invalid amount")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def display(self):
        print("Account Holder:", self.name)
        print("Current Balance:", self.balance)


# 🔹 Using the class
acc = BankAccount("Rahul", 1000)

acc.display()
acc.deposit(500)
acc.withdraw(300)
acc.display()
