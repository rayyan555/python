def is_pythagorean_triple(a, b, c):
    return a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2

# User input
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# Check if it is a Pythagorean triple
if is_pythagorean_triple(a, b, c):
    print("The numbers form a Pythagorean triple.")
else:
    print("The numbers do not form a Pythagorean triple.")
