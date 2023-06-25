# Read the value of 'n' from the user
n = int(input("Enter the number of integers: "))

# Read 'n' integers from the user and generate separate lists for even and odd numbers
even_nums = []
odd_nums = []
for i in range(n):
    num = int(input(f"Enter integer {i+1}: "))
    if num % 2 == 0:
        even_nums.append(num)
    else:
        odd_nums.append(num)

# Display the results
print("Even numbers:", even_nums)
print("Odd numbers:", odd_nums)
