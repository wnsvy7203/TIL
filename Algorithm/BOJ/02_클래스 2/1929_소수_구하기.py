# Silver 3
# 5420ms

import sys


M, N = map(int, sys.stdin.readline().split())
lst = list(range(M, N+1))

for i in lst:
    if i == 1:
        continue

    for j in range(2, int(i**0.5)+1):
        if not i % j:
            break
    else:
        print(i)
