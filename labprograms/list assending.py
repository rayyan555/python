n = int(input("Enter number of elements in list: "))
lst = []

for i in range(n):
    e = int(input("Enter the value: "))
    lst.append(e)

print("Original list:", lst)

ascending = True
for i in range(1, len(lst)):
    if lst[i] < lst[i - 1]:
        ascending = False
        break

if ascending:
    print("The list is in ascending order.")
else:
    print("The list is NOT in ascending order.")
