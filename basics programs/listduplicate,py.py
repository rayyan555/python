# Read the list of numbers from the user
numbers = input("Enter the list of numbers separated by spaces: ").split()

# Create a new list without duplicates using list comprehension
new_list = list(dict.fromkeys(numbers))

# Print the new list without duplicates
print("List without duplicates:", new_list)
