n = int(input("Enter the Number:"))

total = 0
for i in range(0,n+1,2):
    total += i
print(total)

# while loop
total = 0
i = 0
while i <= n:
    if i % 2 == 0:
        total += i
    i += 1
print(total)