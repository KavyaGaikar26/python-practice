def digit_count(n):
    if n < 10:
        return 1
    else:
        return 1+ digit_count(n // 10) 

print(digit_count(12345))