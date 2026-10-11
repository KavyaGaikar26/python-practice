numbers = [0, 1, 0, 3, 12]

non_zeros = []
zeros = []

for num in numbers:
    if num != 0:
        non_zeros.append(num)
    elif num == 0:
        zeros.append(num)

final_list = non_zeros +  zeros

print(final_list)