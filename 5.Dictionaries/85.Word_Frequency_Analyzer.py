text = input("Enter the Text:")

words = text.split()

word_frequency = {}

for word in words:

    if word in word_frequency:
        word_frequency[word] +=1
    else:
        word_frequency[word] = 1

print("Word Frequency:", word_frequency)

max_count = 0
most_frequent = ""

for word, count in word_frequency.items():
    if count > max_count:
        max_count = count
        most_frequent = word

print("Most Frequent:", most_frequent)
print("Count:", max_count)

min_count = float('inf')
least_frequent = ""

for word, count in word_frequency.items():
    if count < min_count:
        min_count = count
        least_frequent = word

print("Least Frequent:", least_frequent)
print("Count:", min_count)