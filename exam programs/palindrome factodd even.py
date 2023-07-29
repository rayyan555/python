n = int(input("enter a number:"))

if n % 2 == 0:
    if str(n) == str(n)[::-1]:
        print("Palindrome")
    else:
        print("Not palindrome")
else:
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("The factorial is:", format(fact))
    print("The number of digits in factorial is:", len(str(fact)))
