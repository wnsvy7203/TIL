# silver 4
# 92ms

from collections import deque

N, K = map(int, input().split())
nums = deque(range(1, N+1))
yo = []

while nums:
    nums.rotate(-K+1)
    yo.append(nums.popleft())

print('<', end='')
print(*yo, sep=', ', end='')
print('>', end='')
