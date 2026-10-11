n = int(input("Enter your Marks:"))

if 90 <= n <= 100:
    print("Your Grade is A")
elif 80 <= n <= 89:
    print("Your Grade is B")
elif 70 <= n <= 79:
    print("Your Grade is C")
elif 60 <= n <= 69:
    print("Your Grade is D")
elif 0 <= n < 60:
    print("Your Grade is F")
elif n < 0:
    print("Marks entered are Invalid")
elif n > 100:
    print("Marks entered are Invalid")
