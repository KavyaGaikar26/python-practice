def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def apply_operation(operation, a, b):
    return operation(a, b)

print(apply_operation(add, 10, 5))
print(apply_operation(subtract, 10, 5))
print(apply_operation(multiply, 10, 5))
