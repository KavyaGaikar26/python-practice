fruits = ["apple", "banana", "mango", "orange"]

for index, fruit in enumerate(fruits):
    print(index, fruit)


# 1. Simple list
# names = ["Kavya", "Rahul", "Priya"]

# for index, name in enumerate(names):
#     print(index, name)

# Output:

# 0 Kavya
# 1 Rahul
# 2 Priya

# 2. Start counting from 1

# By default, counting starts at 0.

# You can change that:

# names = ["Kavya", "Rahul", "Priya"]

# for index, name in enumerate(names, start=1):
#     print(index, name)

# Output:

# 1 Kavya
# 2 Rahul
# 3 Priya

# This is useful for numbered lists.



# 3. Finding the position of something
# fruits = ["apple", "banana", "mango", "orange"]

# for index, fruit in enumerate(fruits):
#     if fruit == "mango":
#         print("Mango is at index", index)

# Output:

# Mango is at index 2
# 4. Printing a numbered menu
# menu = ["Pizza", "Burger", "Pasta", "Sandwich"]

# for number, item in enumerate(menu, start=1):
#     print(number, item)

# Output:

# 1 Pizza
# 2 Burger
# 3 Pasta
# 4 Sandwich

# This is a very practical use.

# 5. Working with strings

# enumerate() doesn't only work with lists.

# word = "Python"

# for index, character in enumerate(word):
#     print(index, character)

# Output:

# 0 P
# 1 y
# 2 t
# 3 h
# 4 o
# 5 n

# So you can use it with any iterable, including strings.

# 6. Modifying something based on its position

# Suppose:

# numbers = [10, 20, 30, 40]

# You want to add the index to each number:

# numbers = [10, 20, 30, 40]

# for index, number in enumerate(numbers):
#     print(number + index)

# Output:

# 10
# 21
# 32
# 43

# Because:

# 10 + 0 = 10
# 20 + 1 = 21
# 30 + 2 = 32
# 40 + 3 = 43
# 7. A very common real-world example

# Suppose you have marks:

# marks = [85, 72, 91, 64]

# You could print:

# for index, mark in enumerate(marks, start=1):
#     print("Student", index, ":", mark)

# Output:

# Student 1 : 85
# Student 2 : 72
# Student 3 : 91
# Student 4 : 64
# 8. enumerate() vs range(len())

# This is probably the most important comparison.

# Old way:

# fruits = ["apple", "banana", "mango"]

# for i in range(len(fruits)):
#     print(i, fruits[i])

# Pythonic way:

# for i, fruit in enumerate(fruits):
#     print(i, fruit)

# The second is generally cleaner and easier to read