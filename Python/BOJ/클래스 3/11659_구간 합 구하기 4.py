# silver 3
# 320ms

import sys

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
sums = [0] * N
sums[0] = nums[0]

for k in range(1, N):
    sums[k] = sums[k-1] + nums[k]


for _ in range(M):
    i, j = map(lambda x: int(x)-1, sys.stdin.readline().split())

    if i == 0:
        print(sums[j])
    else:
        print(sums[j] - sums[i-1])
