a = int(input("Enter the Number:"))
b = int(input("Enter the Number:"))

def gcd(a,b):
    c = min(a,b)
    gcd = 1

    for i in range(1, c+1):

        if a % i == 0 and b % i == 0:
            gcd = i
            
    return gcd

print(gcd(a,b))

