# silver 1
# 0ms

import sys

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = arr[0][0]

for i in range(1, N):
    dp[0][i] = dp[0][i-1] + arr[0][i]
    dp[i][0] = dp[i-1][0] + arr[i][0]

for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = arr[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]


for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    X1, Y1, X2, Y2 = x1-1, y1-1, x2-1, y2-1

    if X1 == 0 and Y1 == 0:
        print(dp[X2][Y2])
    elif X1 == 0 and Y1 != 0:
        print(dp[X2][Y2] - dp[0][Y2])
    elif Y1 == 0 and X1 != 0:
        print(dp[X2][Y2] - dp[X2][0])
    else:
        print(dp[X2][Y2] + dp[X1-1][Y1-1] - dp[X1-1][Y2] - dp[X2][Y1-1])
