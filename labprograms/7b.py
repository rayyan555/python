
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age < 0:
    raise Exception("Error: Age cannot be negative")

marks = []
for i in range(1, 7):
    mark = float(input(f"Enter the mark for subject {i}: "))
    marks.append(mark)

student = {
    "Name": name,
    "Age": age,
    "Marks": marks
}

print("\nGenerated Dictionary:")
print(student)
