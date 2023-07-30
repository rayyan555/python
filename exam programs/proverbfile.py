file_path = 'proverb.txt'
proverb = "Diligence is the mother of good future."

# Append the proverb to the file
with open(file_path, 'a') as file:
    file.write(proverb + "\n")

# Read and display the updated content of the file
with open(file_path, 'r') as file:
    updated_content = file.read()

print("Updated content of 'proverb.txt':")
print(updated_content)

