# Silver 3

import sys

M, N = map(int, sys.stdin.readline().split())
lst = list(range(M, N+1))

for i in range(M, N+1):
    for j in range(2, i):
        if not i % j:
            break
    else:
        print(i)
