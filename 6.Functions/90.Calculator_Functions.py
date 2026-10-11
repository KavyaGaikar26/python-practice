a = int(input("Enter the Number:"))
b = int(input("Enter the Number:"))

def add(a,b):
    add = a + b
    return add

def subtract(a,b):
    subtract = a - b
    return subtract

def multiply(a,b):
    multiply = a * b
    return multiply

def divide(a,b):
    if b != 0:
        divide = a / b
        return divide
    elif b == 0:
        return " Invalid Input"

print("Addition of two numbers is:", add(a,b))
print("Subtraction of two numbers is:", subtract(a,b))
print("Multiplication of two numbers is:", multiply(a,b))
print("Division of two numbers is:", divide(a,b))
