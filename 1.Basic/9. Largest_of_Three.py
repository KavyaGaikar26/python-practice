a = int(input("Enter the Number:"))
b = int(input("Enter the Number:"))
c = int(input("Enter the Number:"))

if a > b and a > c:
    print(f"The Largest Number is {a}")
elif b > a and b > c:
    print(f"The Largest Number is {b}")
elif c > a and c > a:
    print(f"The Largest Number is {c}")
else:
    print("All Numbers are Equal")