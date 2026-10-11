dict1 = {
    "a": 1,
    "b": 2,
    "c": 3
}

dict2 = {
    "b": 20,
    "c": 30,
    "d": 40
}

common = []

for key in dict1:
    if key in dict2:
        common.append(key)

print(common)