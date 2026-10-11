def multiply(a, b):
    return a * b

def add(a, b):
    return a + b

def custom_reduce(function, numbers):
    product = numbers[0]

    for number in numbers[1:]:
        product = function(product, number)

    return product

numbers = [1, 2, 3, 4, 5]

print(custom_reduce(multiply, numbers))

print(custom_reduce(add, [1, 2, 3, 4, 5]))