# Silver 3

import sys


M, N = map(int, sys.stdin.readline().split())
lst = list(range(2, N+1))

for i in range(len(lst)):

    if i == 0:
        print(i)
