# silver 5
# 92ms

from collections import deque

N = int(input())
num = list(map(int, input().split()))

num.sort()
num = deque(num)
if 1 in num:
    num.popleft()
cnt = 0
for i in num:
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        cnt += 1
print(cnt)
