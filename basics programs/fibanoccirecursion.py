def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Read input from the user
n = int(input("Enter the value of n: "))

# Call the Fibonacci function
result = fibonacci(n)

# Print the result
print("The {}th term of the Fibonacci series is: {}".format(n, result))
