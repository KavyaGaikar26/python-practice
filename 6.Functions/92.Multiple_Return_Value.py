numbers = [10, 20, 30, 40]

def get_statistics(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    elements = len(numbers)
    average = total / elements

    return minimum, maximum, total, average

minimum, maximum, total, average = get_statistics(numbers)

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Total:", total)
print("Average:", average)