# bronze 1
# 84ms

N = int(input())
arr = list(map(int, input().split()))
m = max(arr)
for i in range(N):
    arr[i] = arr[i] / m * 100

print(sum(arr)/N)
