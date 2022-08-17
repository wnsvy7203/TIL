import sys
input = sys.stdin.readline

N = int(input()) # 1 <= N <= 100000
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    arr[i][0], arr[i][1] = arr[i][1], arr[i][0]

arr.sort()

for i in range(N):
    arr[i][0], arr[i][1] = arr[i][1], arr[i][0]

for i in range(N):
    print(*arr[i])
