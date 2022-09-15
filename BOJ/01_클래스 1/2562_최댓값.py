# Bronze 3
# 68ms

arr = [int(input()) for _ in range(9)]
print(max(arr))
for i in range(9):
    if arr[i] == max(arr):
        print(i+1)
