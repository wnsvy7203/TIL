# silver 3
# 60ms

import sys
from itertools import combinations_with_replacement


def sort_num(x):
    return x


N, M = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
lst = list(combinations_with_replacement(nums, M))

for i in range(len(lst)):
    lst[i] = tuple(sorted(lst[i], key=sort_num))

for i in sorted(lst):
    print(*i)
