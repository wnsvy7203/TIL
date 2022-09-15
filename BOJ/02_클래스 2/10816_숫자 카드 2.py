# Silver 4
# 1528ms

from bisect import bisect_left, bisect_right
import sys

N = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))
M = int(sys.stdin.readline())
com = list(map(int, sys.stdin.readline().split()))
cnt = [0] * M

for i in range(M):
    cnt[i] = bisect_right(arr, com[i]) - bisect_left(arr, com[i])

print(*cnt)
