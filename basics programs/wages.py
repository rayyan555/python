name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
days_worked = int(input("Enter the number of days worked: "))

wages = 0

if age >= 18 and age > 30 and gender == "M":
    wages = 700
elif age >= 18 and age < 30 and gender == "F":
    wages = 750
elif age >= 30 and age <= 40 and gender == "M":
    wages = 800
elif age >= 30 and age <= 40 and gender == "F":
    wages = 800

total_wages = wages * days_worked

print("Name:", name)
print("Wages per day:", wages)
print("Total Wages:", total_wages)
