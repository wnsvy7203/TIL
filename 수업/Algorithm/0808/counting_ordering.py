N = int(input())
arr = list(map(int, input().split()))

tmp = [0] * N
c = [0] * 101
for i in range(N):
    c[arr[i]] += 1
for i in range(1, 101):
    c[i] += c[i-1]

for i in range(N-1, -1, -1):
    c[arr[i]] -= 1
    tmp[c[arr[i]]] = arr[i]