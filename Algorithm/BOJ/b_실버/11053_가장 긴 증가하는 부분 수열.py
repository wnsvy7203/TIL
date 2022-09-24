# silver 2
# 200ms

import sys

N = int(sys.stdin.readline())
A = [0] + list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
