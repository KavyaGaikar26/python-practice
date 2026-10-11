dict1 = {
    "a": 1,
    "b": 2
}

dict2 = {
    "c": 3,
    "d": 4
}

merged = dict1.copy()

for key, value in dict2.items():
    merged[key] = value

print(merged)



# merged = {**dict1, **dict2}

