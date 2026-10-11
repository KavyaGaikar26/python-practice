numbers = [1, 2, 3, 2, 4, 5, 1, 6]

unique = []
duplicate = []

for num in numbers:
    if num not in unique:
        unique.append(num)
    elif num in unique and num not in duplicate:
        duplicate.append(num)

print(duplicate)