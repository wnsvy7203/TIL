arr = [3, 6, 7, 1, 5, 4]
n = len(arr)
for i in range(n):
    if 0 | (1 << i):
        print(arr[i], end='')
    print()
print()
