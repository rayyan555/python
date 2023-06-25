# Read the value of n from the user
n = int(input("Enter the number of integers (n): "))

# Read n positive integers from the user and store them in a list
numbers = []
for i in range(n):
    num = int(input(f"Enter positive integer {i+1}: "))
    numbers.append(num)

# Check if the list contains any prime numbers
prime_numbers = []
for num in numbers:
    if num < 2:
        continue
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)

contains_primes = len(prime_numbers) > 0

# Print the result
if contains_primes:
    print("True")
    print("Number of prime numbers:", len(prime_numbers))
else:
    print("False")
