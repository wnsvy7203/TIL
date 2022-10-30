# silver 2
# 0ms

import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())

    if a == -1 and b == -1 and c == -1:
        break

    ans = 0

    if a == b == c:
        ans = 2 ** a



    print(f'w({a}, {b}, {c} = {ans}')
