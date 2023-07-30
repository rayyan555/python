class NegativeAgeException(Exception):
    pass

def get_student_details():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))

    if age < 0:
        raise NegativeAgeException("Age cannot be negative.")

    subject_marks = []
    for i in range(6):
        subject_mark = float(input(f"Enter subject {i + 1} mark: "))
        subject_marks.append(subject_mark)

    student_data = {
        "name": name,
        "age": age,
        "subject_marks": subject_marks
    }

    return student_data

try:
    student_details = get_student_details()

    print("\nStudent Details:")
    print(student_details)

except ValueError:
    print("Invalid input! Please enter a valid number.")
except NegativeAgeException as e:
    print(str(e))
except Exception as e:
    print("An error occurred:", str(e))
