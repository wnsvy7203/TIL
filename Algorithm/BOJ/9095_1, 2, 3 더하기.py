# silver 3
# 68ms

import sys


def f(n):
    if n == 1 or n == 2:
        return n
    elif n == 3:
        return n + 1
    else:
        return f(n-1) + f(n-2) + f(n-3)


T = int(sys.stdin.readline())

for _ in range(T):
    print(f(int(sys.stdin.readline())))
