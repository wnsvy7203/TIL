# silver 3
# 96ms

from collections import deque

N, K, M = map(int, input().split())
nums = deque(range(1, N+1))
yo = []

d = 1
while nums:
    if len(yo) and len(yo) % M == 0:
        d *= -1
    nums.rotate(d * (-K+1))
    if d == 1:
        yo.append(nums.popleft())
    else:
        yo.append(nums.pop())

for i in yo:
    print(i)
