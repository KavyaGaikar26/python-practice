def square(n):
    return n * n

def custom_map(function, numbers):
    results = []

    for number in numbers:
        results.append(function(number))

    return results


numbers = [1, 2, 3, 4, 5]

print(custom_map(square, numbers))