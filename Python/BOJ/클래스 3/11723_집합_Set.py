# silver 5
# 6376ms

import sys

M = int(sys.stdin.readline())
S = set()
for _ in range(M):
    cal = sys.stdin.readline().split()
    if len(cal) == 2:
        order, x = cal[0], int(cal[1])

        if order == 'add' and x not in S:
            S.add(x)
        elif order == 'remove' and x in S:
            S.remove(x)
        elif order == 'check':
            if x in S:
                print(1)
            else:
                print(0)
        elif order == 'toggle':
            if x in S:
                S.remove(x)
            else:
                S.add(x)

    if cal == ['all']:
        S = set(i for i in range(1, 21))
    elif cal == ['empty']:
        S = set()
