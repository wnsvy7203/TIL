# gold 5
# 248ms

import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())

    arr = deque(sys.stdin.readline().rstrip()[1:-1].split(','))

    if n == 0:
        arr = deque()

    rev = 0

    flag = True

    for i in p:
        if i == 'R':
            rev += 1

        if i == 'D':
            if arr:
                if rev % 2:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                flag = False
                print('error')
                break

    if flag:
        if rev % 2:
            arr.reverse()
            print('[' + ','.join(arr) + ']')
        else:
            print('[' + ','.join(arr) + ']')