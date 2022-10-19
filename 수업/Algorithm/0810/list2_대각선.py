N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

s = 0
for i in range(N):
    s += arr[i][i]


s = 0
for i in range(N):
    s += arr[i][N-1-i]