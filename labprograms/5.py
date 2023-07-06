
# Define the sets
a = {1, 2, 3, 4}
b = {1, 2, 3}

# Check if set b is a subset of set a
result = all(elem in a for elem in b)

# Print the result
print(result)
