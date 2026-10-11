numbers = [4, 9, 2, 15, 7]

minimum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num

print(minimum)