
file1_path = input("Enter the path of File 1: ")
file2_path = input("Enter the path of File 2: ")

try:
    with open(file2_path, 'r') as file2:
        content = file2.read()

    with open(file1_path, 'a') as file1:
        file1.write(content)

    print("Content added successfully!")
except FileNotFoundError:
    print("Error: File not found.")
