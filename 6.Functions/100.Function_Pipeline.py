def double(x):
    return x * 2

def add_10(x):
    return x + 10

def square(x):
    return x * x

def pipeline(value, *functions):
    result = value

    for function in functions:
        result = function(result)

    return result

print(pipeline(5, double, add_10, square))