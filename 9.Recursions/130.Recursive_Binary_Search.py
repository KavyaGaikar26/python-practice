def recursive_binary_search(numbers, target, left, right):

    if left > right:
        return False

    mid = (left + right) // 2

    if numbers[mid] == target:
        return True

    elif numbers[mid] < target:
        return recursive_binary_search(numbers, target, mid + 1, right)

    else:
        return recursive_binary_search(numbers, target, left, mid - 1)


numbers = [1, 3, 5, 7, 9, 11, 13]

print(recursive_binary_search(numbers, 7, 0, len(numbers) - 1))
print(recursive_binary_search(numbers, 4, 0, len(numbers) - 1))