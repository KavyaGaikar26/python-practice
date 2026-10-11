text = input("Enter a sentence: ")

count = 1

for space in text:
    if space in " ":
        count += 1

print(count)