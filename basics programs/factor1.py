number = int(input("Enter a number: "))

print("Factors of", number, ":", end=" ")
for i in range(1, number + 1):
    if number % i == 0:
        print(i, end=" ")
