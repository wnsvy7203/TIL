# gold 2

import sys

N = int(sys.stdin.readline())
A = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(N+1)]
stk = [(0, 0)]
a = []
n = 0

while True:
    cnt, p = stk[-1][0], stk[-1][1]
    for i in range(1, N+1):
        if p < A[i]:
            cnt += 1
            stk.append((cnt, A[i]))
            break
        else:
            while stk[-1][1] < A[i]:
                b, c = stk.pop()
                a.append((b, c))

    n += 1

    if n == N:
        break
a.sort()
print(a[-1][0])
