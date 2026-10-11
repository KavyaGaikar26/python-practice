text = input("Enter the Text:")

vowel_count = 0

for char in text:
    if char in "aeiou":
        vowel_count += 1

print(vowel_count)