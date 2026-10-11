def flatten_list(numbers):

    result = []

    for item in numbers:

        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)

    return result


numbers = [1, [2, 3], [4, [5, 6]]]

print(flatten_list(numbers))