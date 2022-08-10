arr = [7, 2, 5, 3, 4, 6]
N = len(arr)

for i in range(N-1):
    minIdx = i
    for j in range(i+1, N):
        if arr[minIdx] > arr[j]:
            minIdx = j
    arr[minIdx], arr[i] = arr[i], arr[minIdx]

print(arr)