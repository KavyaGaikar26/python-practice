def average(*numbers):

    if len(numbers) == 0:
        return "The list is empty. Cannot calculate statistics."
    
    total = sum(numbers)
    elements = len(numbers)
    average = total / elements

    return average


print(average(10, 20))
print(average(10, 20, 30, 40))
print(average())
print(average(5, 10, 15, 20, 25))



