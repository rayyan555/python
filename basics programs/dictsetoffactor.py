start = 1
end = 9

factors_dict = {}

for num in range(start, end+1):
    factors_dict[num] = {i for i in range(1, num+1) if num % i == 0}

print(factors_dict)
