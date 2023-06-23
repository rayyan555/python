def calculate_power(base, power):
    result = base ** power
    return result

# Read input from the user
base = int(input("Base: "))
power = int(input("Power: "))

# Call the calculate_power function
output = calculate_power(base, power)

# Print the result
print(output)
