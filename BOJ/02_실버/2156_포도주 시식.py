# silver 1
# 84ms

import sys

N = int(sys.stdin.readline())

glass = [0 for _ in range(10000)]
for i in range(N):
    glass[i] = int(sys.stdin.readline())

dp = [0 for _ in range(10000)]

dp[0] = glass[0]
dp[1] = glass[0] + glass[1]
dp[2] = max(glass[0] + glass[2], glass[1] + glass[2], dp[1])

for i in range(3, N):
    dp[i] = max(glass[i] + dp[i-2], glass[i] + glass[i-1] + dp[i-3], dp[i-1])

print(dp[N-1])
