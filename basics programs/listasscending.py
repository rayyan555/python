# Read integers from the user and store them in a list
numbers = []
while True:
    num = int(input("Enter an integer (0 to stop): "))
    if num == 0:
        break
    numbers.append(num)

# Sort the list in ascending order
numbers.sort()

# Display the sorted list
print("Sorted values:", numbers)
