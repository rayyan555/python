# Read the list of 5 numbers from the user
numbers = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Calculate the factorial of each number and store them in a new list
factorials = []
for num in numbers:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    factorials.append(factorial)

# Print the resulting list of factorials
print("Factorials:", factorials)
