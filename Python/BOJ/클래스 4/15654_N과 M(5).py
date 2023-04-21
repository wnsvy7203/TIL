# silver 3
# 164ms

import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

for i in sorted(permutations(nums, M)):
    print(*i)
