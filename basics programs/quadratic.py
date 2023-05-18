def solve_equation(x, y):
    z = abs(x - y) * (x + y)
    return z

# Taking input from the user
x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))

# Solving the equation and printing the result
result = solve_equation(x, y)
print("The value of z is:", result)
