list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = []

for num in list1:
    if num in list2:
        common.append(num)

print(common)

set1 = set(list1)
set2 = set(list2)

common_set = set1.intersection(set2)

print(list(common_set))
