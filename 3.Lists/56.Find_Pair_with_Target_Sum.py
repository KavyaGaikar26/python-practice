numbers = [1, 5, 3, 7, 9, 2]
target = 10

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print([numbers[i], numbers[j]])