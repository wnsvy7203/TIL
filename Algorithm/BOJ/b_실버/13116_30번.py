# Silver 4
# 892ms

import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    nums = list(range(1, 1024))

    a = A
    b = B

    while a != b:
        if a < b:
            b //= 2
        else:
            a //= 2

    print(a * 10)
