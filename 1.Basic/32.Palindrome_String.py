text = input("Enter a string: ")

reverse = ""

for char in text:
    reverse = char + reverse

print(reverse)

if reverse == text:
    print("It is a Palindrome String")  
else:
    print("It is not a Palindrome String")