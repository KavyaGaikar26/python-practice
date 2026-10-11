a = int(input("Enter the Number:"))
b = int(input("Enter the Number:"))

def lcm(a,b):
    c = max(a,b)

    while True:
        if c % a == 0 and c % b == 0:
            return c

        c += 1

print(lcm(a,b))
