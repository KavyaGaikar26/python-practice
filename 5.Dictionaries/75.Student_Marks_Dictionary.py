marks = {
    "Kavya": 92,
    "Rahul": 84,
    "Aman": 76
}

highest_student = ""
highest_score = 0

lowest_student = ""
lowest_score = float("inf")

total = 0

for student, mark in marks.items():
    if mark > highest_score:
        highest_score = mark
        highest_student = student

    if mark < lowest_score:
        lowest_score = mark
        lowest_student = student

    total += mark

average = total / len(marks)

print("Highest Scorer:", highest_student, highest_score)
print("Lowest Scorer:", lowest_student, lowest_score)
print("Average:", average)