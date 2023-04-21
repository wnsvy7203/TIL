# silver 1
# 268ms

import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()

cnt = 0
step = 0
ans = 0

while step < M - 1:
    if S[step:step+3] == 'IOI':
        cnt += 1
        step += 2
        if cnt == N:
            ans += 1
            cnt -= 1
    else:
        step += 1
        cnt = 0

print(ans)
