# gold 5
# 740ms

import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

a, b = len(A), len(B)

dp = [[0 for _ in range(1001)] for _ in range(1001)]

for i in range(1, a+1):
    for j in range(1, b+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[a][b])
