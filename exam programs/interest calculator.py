def interest_calculation(p,n,r):
    return (p*n*r)/100
    
name = input("Enter the name: ")
age = int(input("Enter your age: "))
gen = input("Your Gender (Male = M and Female = F): ")
p = int(input("Enter your principle amount: "))
n = int(input("Enter the number of years: "))

if age > 60:
    print("Simple Interest will be ",interest_calculation(p,n,12)," at rate of interest as 12%")
elif gen == 'f' or gen == 'F':
    print("Simple Interest will be ",interest_calculation(p,n,10)," at rate of interest as 10%")
else:
    print("Simple Interest will be ",interest_calculation(p,n,9)," at rate of interest as 9%")
