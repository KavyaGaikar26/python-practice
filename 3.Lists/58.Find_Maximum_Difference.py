numbers = [10, 3, 8, 20, 5]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

for num in numbers:
    if num < smallest:
        smallest = num

maximum_difference = largest - smallest

print(maximum_difference)