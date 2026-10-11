n = int(input("Enter the Number:"))

sum = 0

while n > 0:
    digit = n % 10
    sum += digit
    n = n // 10
    
print(sum)