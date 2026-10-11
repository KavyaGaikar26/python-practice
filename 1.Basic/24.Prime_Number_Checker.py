n = int(input("Enter the Number:"))
if n <= 1:
    print("It is not Prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("It is not Prime")
            break
    else:
        print("It is Prime")