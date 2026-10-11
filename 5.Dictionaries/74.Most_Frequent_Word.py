text = input("Enter the Text:")

words = text.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

max_count = 0
most_frequent = ""

for word, count in frequency.items():
    if count > max_count:
        max_count = count
        most_frequent = word

print("Most Frequent Word:", most_frequent)
print("Frequency:", max_count)
