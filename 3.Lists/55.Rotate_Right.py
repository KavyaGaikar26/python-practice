numbers = [1, 2, 3, 4, 5]

k = int(input("Enter the Value of 'k':"))
k = k % len(numbers)
m = len(numbers) - k

set_2 = numbers[:m]
set_1 = numbers[m:]

rotated = set_1 + set_2

print(rotated)