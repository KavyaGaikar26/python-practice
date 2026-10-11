numbers = [1, 2, 2, 3, 1, 4, 5, 3, 4, 5, 6, 7, 8, 9, 10]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)