# Read the string from the user
string = input("Enter the string: ")

# Encode each character using ASCII values and store them in a list
ascii_list = [ord(char) for char in string]

# Print the encoded list
print("Encoded List:", ascii_list)
