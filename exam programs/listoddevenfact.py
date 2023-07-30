n=int(input("enter number of elements in the list: "))
a=[int(input()) for i in range(n)]
print("the given list is ",a)
od=[]
eve=[]
od=[j for j in a if (j%2!=0)]
eve=[k for k in a if (k%2==0)]
print("odd numbers ",od)
print("even numbers ",eve)
def factorial(i):
    fact=1
    for j in range(1,i+1):
        fact*=j 
    return fact
print("enter 5 integers")
a=[int(input()) for i in range(5)]
f=[factorial(i) for i in a]
print("the given list is ",a)
print("factorial of the list is ",f)
