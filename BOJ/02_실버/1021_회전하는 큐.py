# silver 3
# 88ms

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
find = list(map(int, sys.stdin.readline().split()))
nums = deque(range(1, N+1))

cnt = 0
for i in find:
    while True:
        if nums[0] == i:
            nums.popleft()
            break
        else:
            if nums.index(i) <= len(nums) // 2:
                nums.rotate(-1)
                cnt += 1
            else:
                nums.rotate(1)
                cnt += 1

print(cnt)
