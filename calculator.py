# Simple Calculator Program
while True:
# Take input from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Choose operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter choice (1/2/3/4): ")

# Perform calculation
    if choice == '1':
        result = num1 + num2
        print("Result:", result)
        continue

    elif choice == '2':
        result = num1 - num2
        print("Result:", result)
        continue

    elif choice == '3':
        result = num1 * num2
        print("Result:", result)
        continue

    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
            continue
        else:
            print("Error! Division by zero is not allowed.")

    else:
        print("Invalid choice! Please select 1, 2, 3, or 4.")
