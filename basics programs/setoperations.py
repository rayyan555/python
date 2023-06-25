def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

primes = {num for num in range(1, 51) if is_prime(num)}
divisible_by_5 = {num for num in range(1, 51) if num % 5 == 0}

print("Prime numbers:", primes)
print("Numbers divisible by 5:", divisible_by_5)

union_set = primes.union(divisible_by_5)
intersection_set = primes.intersection(divisible_by_5)
difference_set = primes.difference(divisible_by_5)
symmetric_difference_set = primes.symmetric_difference(divisible_by_5)

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference (Prime - Divisible by 5):", difference_set)
print("Symmetric Difference:", symmetric_difference_set)
