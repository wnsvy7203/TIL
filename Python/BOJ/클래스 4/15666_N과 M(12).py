# silver 2
# 52ms

import sys
from itertools import combinations_with_replacement as combi


def sorted_nums(x):
    return x


N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
lst = list(set(combi(nums, M)))

for i in range(len(lst)):
    lst[i] = tuple(sorted(lst[i], key=sorted_nums))

for i in sorted(list(set(lst))):
    print(*i)
