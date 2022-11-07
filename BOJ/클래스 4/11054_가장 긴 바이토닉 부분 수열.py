# gold 4
# 336ms

import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

dp_left = [1 for _ in range(N)]
dp_right = [1 for _ in range(N)]
dp = [0 for _ in range(1001)]

for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp_left[i] = max(dp_left[i], dp_left[j] + 1)

for i in range(N-1, -1, -1):
    for j in range(N-1, i-1, -1):
        if nums[i] > nums[j]:
            dp_right[i] = max(dp_right[i], dp_right[j] + 1)

for i in range(N):
    dp[i] = dp_left[i] + dp_right[i]

print(max(dp)-1)
