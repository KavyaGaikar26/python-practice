numbers = [3, 7, 2, 9, 5]

def recursive_max(numbers):
    if len(numbers) == 1:
        return numbers[0]

    rest_max = recursive_max(numbers[1:])

    if numbers[0] > rest_max:
        return numbers[0]
    else:
        return rest_max

numbers = [3, 7, 2, 9, 5]

print(recursive_max(numbers))
    