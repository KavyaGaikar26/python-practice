numbers = [-5, 10, -2, 7, -8]

positive_sum = 0
negative_sum = 0

for num in numbers:
    if num > 0:
        positive_sum += num

    elif num < 0:
        negative_sum += num

print(positive_sum)
print(negative_sum)