start = int(input("Start: "))
end = int(input("End: "))

primes = []
for number in range(start, end + 1):
    if number > 1:
        is_prime = True
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)

print("Prime numbers:", ", ".join(map(str, primes)))
