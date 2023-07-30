def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

print("Simple Calculator")
print("Operations:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    try:
        choice = int(input("Enter operation choice (1/2/3/4) or 0 to exit: "))
        if choice == 0:
            print("Exiting the calculator. Goodbye!")
            break
        elif choice not in [1, 2, 3, 4]:
            print("Invalid choice. Please choose a valid operation.")
            continue

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == 1:
            result = add(num1, num2)
            print("Result:", result)
        elif choice == 2:
            result = subtract(num1, num2)
            print("Result:", result)
        elif choice == 3:
            result = multiply(num1, num2)
            print("Result:", result)
        elif choice == 4:
            try:
                result = divide(num1, num2)
                print("Result:", result)
            except ValueError as e:
                print("Error:", e)
        else:
            print("Invalid choice. Please choose a valid operation.")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
