def interest_calculation(principal, years, rate):
    interest = (principal * years * rate) / 100
    return interest

name = input("Enter customer name: ")
age = int(input("Enter customer age: "))
gender = input("Enter customer gender ('M' or 'F'): ")
principal_amount = float(input("Enter principal amount: "))
num_of_years = int(input("Enter number of years: "))

if age >= 60:
    interest_rate = 12
elif gender.upper() == 'F':
    interest_rate = 10
else:
    interest_rate = 9

interest = interest_calculation(principal_amount, num_of_years, interest_rate)

print("Customer Name:", name)
print("Principal Amount:", principal_amount)
print("Number of Years:", num_of_years)
print("Rate of Interest:", interest_rate, "%")
print("Simple Interest:", interest)
