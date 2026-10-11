numbers = [[1, 2], [3, 4], [5, 6]]

flattened = [number for sublist in numbers for number in sublist]

print(flattened)
