s=int(input("Enter start range: "))
e=int(input("Enter end range: "))
for n in range(s,e+1):
    for i in range(2,n):
     if n%i==0:
        break
    else:
        print(n)
