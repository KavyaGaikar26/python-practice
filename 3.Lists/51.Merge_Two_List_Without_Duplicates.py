list1 = [1, 2, 3]
list2 = [3, 4, 5]

merge_list = list1 + list2

final_merge_list = list(set(merge_list))

print(final_merge_list)