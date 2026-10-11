n = int(input("Enter the Number:"))

sum = 0
i = 1

#for loop
for i in range(1, n + 1):
    sum += i
print(sum)

#while loop
while i <= n:
    sum += i
    i += 1
print(sum)