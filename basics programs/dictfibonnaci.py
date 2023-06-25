fib_dict = {}

def fibonacci(n):
    if n in fib_dict:
        return fib_dict[n]
    elif n <= 1:
        fib_dict[n] = n
    else:
        fib_dict[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fib_dict[n]

input_num = int(input("Enter a number: "))
fib_num = fibonacci(input_num)
print("Fibonacci number:", fib_num)
