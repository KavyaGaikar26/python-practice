n = int(input("Enter the Number:"))

original = n
sum_of_cube = 0

while n > 0:
    digit = n % 10
    sum_of_cube += (digit)**3
    n = n // 10

if sum_of_cube == original:
    print("It is an Armstrong Number")
    