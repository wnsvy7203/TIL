# silver 2
# 132ms

import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(N)]

dp[0] = nums[0]
for i in range(1, N):
    dp[i] = max(nums[i], nums[i] + dp[i-1])

print(max(dp))
