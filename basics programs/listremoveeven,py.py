# Read the list of numbers from the user
numbers = [5, 6, 2, 8, 9, 12, 66]

# Remove even numbers from the list using list comprehension
new_list = [num for num in numbers if num % 2 != 0]

# Print the new list without even numbers
print("List without even numbers:", new_list)
