# 14.Write a menu-driven program using if-elif and loops.
while True:
    print("\n--- MENU ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Exiting program...")
        break

    if choice in [1, 2, 3, 4]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", a + b)
        elif choice == 2:
            print("Result:", a - b)
        elif choice == 3:
            print("Result:", a * b)
        elif choice == 4:
            if b != 0:
                print("Result:", a / b)
            else:
                print("Cannot divide by zero!")
    else:
        print("Invalid choice! Please try again.")