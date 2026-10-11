numbers = [1, 2, 3, 4, 5]

k = int(input("Enter the Value of 'k':"))
k = k % len(numbers)

set_1 = numbers[:k]
set_2 = numbers[k:]

rotated = set_2 + set_1

print(rotated)
