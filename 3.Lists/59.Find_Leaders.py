numbers = [16, 17, 4, 3, 5, 2]

leaders = []

for i in range(len(numbers)):

    is_leader = True

    for j in range(i+1,len(numbers)):

        if numbers[i] < numbers[j]:
            is_leader = False
            break
        
    if is_leader:
        leaders.append(numbers[i])

print(leaders)
