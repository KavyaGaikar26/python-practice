marks = {
    "Kavya": {
        "Math": 95,
        "Physics": 82
    },
    "Rahul": {
        "Math": 88,
        "Physics": 76
    }
}

for student, subjects in marks.items():

    total = 0

    for subject, mark in subjects.items():
        total += mark

    average = total / len(subjects)

    print(student)
    print("Total:", total)
    print("Average:", average)
    print()