# silver 3
# 80ms

from itertools import combinations_with_replacement

N, M = map(int, input().split())
nums = list(range(1, N+1))

for i in combinations_with_replacement(nums, M):
    print(*i)
