students = {
    "Kavya": 92,
    "Rahul": 84,
    "Aman": 76,
    "Priya": 89
}

def get_marks(student):
    return student[1]

sorted_students = sorted(students.items(), key=get_marks)

for student, marks in sorted_students:
    print(student, marks)