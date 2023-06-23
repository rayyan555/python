def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def calculate_series_1(n):
    series_sum = 0
    for i in range(1, n+1):
        series_sum += i / factorial(i)
    return series_sum

def calculate_series_2(n, x):
    series_sum = 0
    denominator = 2
    for i in range(1, n+1):
        series_sum += x / denominator
        denominator *= 2
    return series_sum

def calculate_series_3(n):
    series_sum = 0
    value = 15
    for i in range(1, n+1):
        series_sum += value
        value += 15
    return series_sum

# Read input from the user
n = int(input("Number of terms (n): "))

# Calculate and print the result for series 1
result_1 = calculate_series_1(n)
print("Series 1: {:.4f}".format(result_1))

# Read input from the user for series 2
x = int(input("Value of x: "))

# Calculate and print the result for series 2
result_2 = calculate_series_2(n, x)
print("Series 2: {:.4f}".format(result_2))

# Calculate and print the result for series 3
result_3 = calculate_series_3(n)
print("Series 3: {:.4f}".format(result_3))
