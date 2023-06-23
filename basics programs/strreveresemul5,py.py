def process_string(string):
    length = len(string)

    if length % 5 == 0:
        string = string[::-1]  # Reverse the string
        string = string.upper()  # Capitalize all characters

    return string, length

# Read input from the user
input_string = input("Enter a string: ")

# Call the process_string function
processed_string, string_length = process_string(input_string)

# Print the result
print("Processed string:", processed_string)
print("Length of the string:", string_length)
