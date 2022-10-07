# silver 3
# 72ms

from itertools import combinations

N, M = map(int, input().split())
nums = [i for i in range(1, N+1)]
for i in combinations(nums, M):
    print(*i)
