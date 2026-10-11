numbers = [1, 2, 2, 3, 4, 4, 5]

unique = []

for num in numbers:
    if numbers.count(num) == 1:
        unique.append(num)

print(unique)