# silver 4
# 92ms

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

n = 0
if N > M:
    n = M
else:
    n = N

rec = []

while n > 0:
    for i in range(N-n+1):
        for j in range(M-n+1):
            if arr[i][j] == arr[i][j+n-1] == arr[i+n-1][j] == arr[i+n-1][j+n-1]:
                rec.append(n**2)
    n -= 1

print(max(rec))
