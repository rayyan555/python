squares = {num ** 2 for num in range(1, 31)}
divisible_by_3 = [num for num in range(1, 31) if num % 3 == 0]

new_set = squares - set(divisible_by_3)

print("Square set:", squares)
print("Numbers divisible by 3:", divisible_by_3)
print("New set:", new_set)
