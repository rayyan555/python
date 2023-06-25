numbers = input("Enter a list of numbers (comma-separated): ")
numbers = [int(num) for num in numbers.split(',')]

positive_numbers = tuple(num for num in numbers if num > 0)

print("Positive Numbers:", positive_numbers)
