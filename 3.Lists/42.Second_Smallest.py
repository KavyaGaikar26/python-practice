numbers = [10, 25, 7, 40, 18]

smallest = numbers[0]
second_smallest = numbers[0]

for num in numbers:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest:
        second_smallest = num

print(second_smallest)