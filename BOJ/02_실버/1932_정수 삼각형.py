# silver 1
# 172ms

import sys

N = int(sys.stdin.readline())
dp = []

for i in range(N):
    if i == 0:
        dp.append([int(sys.stdin.readline())])
    else:
        dp.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, N):
    dp[i][0] += dp[i-1][0]
    dp[i][-1] += dp[i-1][-1]
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j]

print(max(dp[-1]))
