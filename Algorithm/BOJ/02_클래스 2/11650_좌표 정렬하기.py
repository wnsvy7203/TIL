# Silver 5
# 4388ms

N = int(input())            # 1 <= N <= 100000

arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort()

for i in range(N):
    print(*arr[i])
