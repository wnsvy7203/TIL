# silver 1
# 68ms

import sys

N = int(sys.stdin.readline())
dp = []
for _ in range(N):
    r, g, b = map(int, sys.stdin.readline().split())
    dp.append([r, g, b])

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + dp[i][0]
    dp[i][1] = min(dp[i-1][2], dp[i-1][0]) + dp[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + dp[i][2]

print(min(dp[-1]))
