
def check_ascending_order(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i-1]:
            return False
    return True

# Read the list of numbers
n = int(input("Enter number of elements in list: "))
numbers = []
for i in range(n):
    num = int(input(f"Enter the value for element {i+1}: "))
    numbers.append(num)

# Check if the list is in ascending order
if check_ascending_order(numbers):
    print("Yes, the list is in ascending order.")
else:
    print("No, the list is not in ascending order.")
