# silver 2
# 100ms

import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

lst = sorted(list(set(permutations(nums, M))))
for i in lst:
    print(*i)
