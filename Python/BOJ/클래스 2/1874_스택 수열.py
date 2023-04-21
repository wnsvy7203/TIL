# silver 2
# 224ms

import sys
N = int(sys.stdin.readline())
cnt = 0
stk = []
cal = []
flag = True

for _ in range(N):
    a = int(sys.stdin.readline())

    while cnt < a:
        cnt += 1
        stk.append(cnt)
        cal.append('+')

    if stk[-1] == a:
        stk.pop()
        cal.append('-')
    else:
        flag = False
        break

if flag:
    print(*cal)
else:
    print('NO')
