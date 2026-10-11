numbers = [10, 20, 30, 40]

def statistics(numbers):

    if len(numbers) == 0:
        return "The list is empty. Cannot calculate statistics."
    
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    elements = len(numbers)
    average = total / elements

    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Total:", total)
    print("Average:", average)

statistics(numbers)
