students = {
    "Kavya": 99,
    "Rahul": 84,
    "Aman": 76,
    "Priya": 68,
    "Riya": 89
}

group = {}

for student, marks in students.items():

    if marks >= 90:
        grade = "A"

    elif marks >= 80:
        grade = "B"

    elif marks >= 70:
        grade = "C"

    else:
        grade = "D"

    if grade not in group:
        group[grade] = []

    group[grade].append(student)

print(group)