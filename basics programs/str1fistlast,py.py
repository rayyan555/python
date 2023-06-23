def string_combination(string):
    if len(string) < 2:
        return ""
    else:
        return string[:2] + string[-2:]

# Read input from the user
input_string = input("Enter a string: ")

# Call the string_combination function
output_string = string_combination(input_string)

# Print the result
print("Output string:", output_string)
