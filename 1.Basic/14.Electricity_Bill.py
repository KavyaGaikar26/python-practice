n = int(input("Enter the Units of Electricity Consumed:"))

if 0 <= n <= 100:
    a = n*5
    print(f"Your Electricity Bill Amount is {a} rupees")
elif 101 <= n <= 200:
    b = n*7
    print(f"Your Electricity Bill Amount is {b} rupees")
elif 201 <= n <= 300:
    c = n*10
    print(f"Your Electricity Bill Amount is {c} rupees")
elif 300 < n:
    d = n*15
    print(f"Your Electricity Bill Amount is {d} rupees")