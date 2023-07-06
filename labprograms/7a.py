
numbers = input("Enter a list of numbers (space-separated): ").split()

try:
    index = int(input("Enter an index: "))
    element = numbers[index]
    print("Element at index", index, "is", element)
except IndexError:
    print("Error: Index is out of range")
