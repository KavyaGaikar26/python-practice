marks = [85, 72, 91, 64, 78]

any(mark < 40 for mark in marks)
print(any(mark < 40 for mark in marks))

all(mark >= 40 for mark in marks)
print(all(mark >= 40 for mark in marks))
