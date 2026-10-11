def factorial(n):
    if n < 0:
        return "invalid input"
    
    elif 0 <= n <= 1:
        return 1

    result = 1

    for i in range(2,n+1):
        result = result * i
        
    return result

number = int(input("Enter the number:"))

print(factorial(number))
