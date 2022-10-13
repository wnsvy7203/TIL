# gold 5
# 0ms

import sys
from math import ceil

C, N = map(int, sys.stdin.readline().split())
dp = [0 for _ in range(C+1)]
city = []
for _ in range(N):
    cost, cnt = map(int, sys.stdin.readline().split())
    city.append((cost, cnt))

for i in range(1, C+1):
    for j in range(N):
        if i - city[j][1] >= 0:
            dp[i] = min(dp[i-city[j][0]] + city[j][1])

print(dp[C])
