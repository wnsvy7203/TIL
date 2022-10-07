# silver 1
# 72ms

import sys

N, D = map(int, sys.stdin.readline().split())
way = []
for _ in range(N):
    way.append(list(map(int, sys.stdin.readline().split())))

way.sort()
dp = [i for i in range(D+1)]


for i in way:
    u, v, w = i
    if v <= D and v - u >= w:
        dp[v] = min(dp[u] + w, dp[v])

    for j in range(u, D+1):
        dp[j] = min(dp[j-1]+1, dp[j])

print(dp[-1])
