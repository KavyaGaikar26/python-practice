def is_even(n):
    return n % 2 == 0
    

def custom_filter(function, numbers):
    even_numbers = []

    for number in numbers:
        if function(number):
            even_numbers.append(number)

    return even_numbers

numbers = [1, 2, 3, 4, 5, 6]

print(custom_filter(is_even, numbers))

    
