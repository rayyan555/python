
file_path = input("Enter the file path: ")
n = int(input("Enter the number of lines to read: "))

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines[:n]:
            print(line.strip())
except FileNotFoundError:
    print("Error: File not found.")
