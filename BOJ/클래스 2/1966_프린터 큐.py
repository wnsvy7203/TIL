# silver 3
# 100ms

from collections import deque
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    que = deque([(v, idx) for idx, v in enumerate(map(int, sys.stdin.readline().split()))])

    cnt = 0
    while True:
        if max(que)[0] == que[0][0]:
            cnt += 1
            if que[0][1] == M:
                print(cnt)
                break
            else:
                que.popleft()
        else:
            que.append((que.popleft()))

