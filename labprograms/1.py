
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_palindrome(number):
    number_str = str(number)
    return number_str == number_str[::-1]

# Get the integer input from the user
number = int(input("Enter an integer number: "))

if number % 2 == 1:  # Odd number
    fact = factorial(number)
    num_digits = len(str(fact))
    print(f"The factorial of {number} is {fact}.")
    print(f"The number of digits in the factorial is {num_digits}.")
else:  # Even number
    if is_palindrome(number):
        print(f"The number {number} is a palindrome.")
    else:
        print(f"The number {number} is not a palindrome.")
