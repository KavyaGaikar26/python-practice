n = int(input("Enter the Number:"))

original = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10 

if original == reverse:
    print("It is a Palindrome Number")
else:
    print("It is not a Palindrome Number")
