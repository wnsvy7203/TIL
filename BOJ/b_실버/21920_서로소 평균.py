# Silver 4
# 1532ms

import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
X = int(input())

total = 0
cnt = 0

for i in A:
    b = max(i, X)
    s = min(i, X)

    while True:
        temp = b
        b = s
        s = temp % b

        if s == 0 and b == 1:
            total += i
            cnt += 1
            break
        elif s == 0 and b != 1:
            break
else:
    print(total / cnt)
