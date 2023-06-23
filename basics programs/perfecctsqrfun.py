number = int(input("Enter a number: "))

is_perfect_square = number >= 0 and int(number ** 0.5) ** 2 == number

if is_perfect_square:
    print(f"{number} is a perfect square.")
else:
    print(f"{number} is not a perfect square.")
