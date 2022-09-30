# silver 5
# 3980ms

import sys

M = int(sys.stdin.readline())
S = []
for _ in range(M):
    cal = list(sys.stdin.readline().split())

    if cal[0] == 'add' and int(cal[1]) not in S:
        S.append(int(cal[1]))
    elif cal[0] == 'remove' and int(cal[1]) in S:
        S.remove(int(cal[1]))
    elif cal[0] == 'check':
        if int(cal[1]) in S:
            print(1)
        else:
            print(0)
    elif cal[0] == 'toggle':
        if int(cal[1]) in S:
            S.remove(int(cal[1]))
        else:
            S.append(int(cal[1]))
    elif cal == ['all']:
        S = list(range(1, 21))
    elif cal == ['empty']:
        S = []
