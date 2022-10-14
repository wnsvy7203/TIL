# gold 5
# 352ms

import sys

n, k = map(int, sys.stdin.readline().split())
val = sorted(list(int(sys.stdin.readline()) for _ in range(n)))
for i in range(n):
    if val[i] > k:
        val = val[:i]
        break
val = sorted(list(set(val)))

dp = [float('inf')] * 20000
dp[0] = 0
for i in range(1, k+1):
    for j in val:
        if j > i:
            break
        if dp[i] > dp[i-j]:
            dp[i] = dp[i-j] + 1

for i in range(1, k+1):
    if dp[i] == float('inf'):
        dp[i] = -1

print(dp[k])
