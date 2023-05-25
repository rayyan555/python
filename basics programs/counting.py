even_count = 0
odd_count = 0

while True:
    num = int(input("Enter the number: "))
    
    if num == -1:
        break
    
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Number of Even Numbers Entered:", even_count)
print("Number of Odd Numbers Entered:", odd_count)
