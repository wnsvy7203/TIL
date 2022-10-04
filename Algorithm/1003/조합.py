arr = [1, 2, 3]
result = []


for i in range(1 << len(arr)):
    subset = []
    for j in range(len(arr)):
        if i & (1 << j):
            subset.append(arr[j])
    if len(subset) == 2:
        result.append(subset)

for i in result:
    print(*i)
