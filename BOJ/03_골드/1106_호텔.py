# gold 5
# 76ms

import sys

C, N = map(int, sys.stdin.readline().split())
dp = [float('inf') for _ in range(1101)]
dp[0] = 0

city = []
for _ in range(N):
    cost, cnt = map(int, sys.stdin.readline().split())
    city.append((cost, cnt))

city.sort()

for cost, cnt in city:
    for j in range(cnt, C+101):
        dp[j] = min(dp[j], dp[j-cnt] + cost)

print(min(dp[C:]))
