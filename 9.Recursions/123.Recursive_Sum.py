0, 1, 1, 2, 3, 5, 8, 13, 21, 34

def recursive_sum(n):
    if n == 1:
        return 1
    else:
        return recursive_sum(n - 1) + n

print(recursive_sum(5))  # Output: 15    
