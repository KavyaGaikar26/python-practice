text = input("Enter the Text:")

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

max_count = 0
most_frequent = ""

for char, count in frequency.items():
    if count > max_count:
        max_count = count
        most_frequent = char

#"Go through everything,
# remember the biggest value I've seen,
# and remember which key produced it."

print("Most frequent character:", most_frequent)
print("Frequency:", max_count)



