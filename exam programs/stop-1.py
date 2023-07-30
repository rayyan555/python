even_count = 0
odd_count = 0

while True:
    number = int(input("Enter the number: "))
    if number == -1:
        break
    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Number of Even Numbers Entered =", even_count)
print("Number of Odd Numbers Entered =", odd_count)
  
