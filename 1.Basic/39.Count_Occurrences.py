numbers = [1, 2, 3, 2, 4, 2, 2, 2]
target = 2

count = 0

for num in numbers:
    if target == num :
        count += 1

print(count)