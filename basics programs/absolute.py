def solve_equation(x, y):
    z = abs(x*y) * (x + y)
    return z

# User input
x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))

# Solve the equation
solution = solve_equation(x, y)
print("Solution:", solution)
