
numbers = [int(num.strip()) for num in input("Enter the list of numbers, separated by commas: ").split(",")]
target = int(input("Enter the element to be found: "))

positive_index = [i+1 for i, num in enumerate(numbers) if num == target]
negative_index = [i-len(numbers)+1 for i, num in enumerate(numbers) if num == target]
count = len(positive_index)

print(f"Element {target} occurs {count} times in the list.")
print("Positive Index:", positive_index)
print("Negative Index:", negative_index)
