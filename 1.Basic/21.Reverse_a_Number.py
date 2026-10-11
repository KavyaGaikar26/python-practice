n = int(input("Enter the Number:"))

reverse = 0

while n > 0:
    digit = n % 10                        #used to find remainder
    reverse = reverse * 10 + digit        #used to build the reversed number
    n = n // 10                           #used to remove the last digit

print(reverse)



# 12345

# Initially:
# n = 12345
# reverse = 0

# Iteration 1:
# digit = 12345 % 10 = 5
# reverse = 0 × 10 + 5 = 5
# n = 12345 // 10 = 1234

# Iteration 2:
# digit = 4
# reverse = 5 × 10 + 4 = 54
# n = 123

# Iteration 3:
# digit = 3
# reverse = 54 × 10 + 3 = 543
# n = 12

# Iteration 4
# digit = 2
# reverse = 543 × 10 + 2 = 5432
# n = 1

# Iteration 5:
# digit = 1
# reverse = 5432 × 10 + 1 = 54321
# n = 0

# Now:
# while n > 0:
# is false, so the loop ends.

# Output:

# Reversed number: 54321
# 🔑 The two operations to remember
# digit = n % 10
# Extract the last digit

# and

# n = n // 10
# Remove the last digit

# Then the clever part:
# reverse = reverse * 10 + digit