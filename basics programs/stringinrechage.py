def swap_and_combine(string1, string2):
    return string2[:2] + string1[2:] + " " + string1[:2] + string2[2:]

# Read input from the user
input_string1 = input("Enter the first string: ")
input_string2 = input("Enter the second string: ")

# Call the swap_and_combine function
output_string = swap_and_combine(input_string1, input_string2)

# Print the result
print("Output string:", output_string)
