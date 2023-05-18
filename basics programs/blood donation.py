def check_eligibility(name, age, weight):
    return age > 18 and weight > 40

name = input("Enter your name: ")
age = int(input("Enter your age: "))
weight = int(input("Enter your weight (in kg): "))

eligibility = check_eligibility(name, age, weight)

if eligibility:
    print(f"Congratulations, {name}! You are eligible for the blood donation camp.")
else:
    print(f"Sorry, {name}, but you are not eligible for the blood donation camp.")
