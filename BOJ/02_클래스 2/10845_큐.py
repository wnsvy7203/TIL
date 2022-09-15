# Silver 4
# 100ms

import sys
from collections import deque

N = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().split()) for _ in range(N)]
queue = deque()

for i in arr:
    if i[0] == 'push':
        queue.append(i[1])

    if i == ['pop']:
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif i == ['size']:
        print(len(queue))
    elif i == ['empty']:
        if queue:
            print(0)
        else:
            print(1)
    elif i == ['front']:
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif i == ['back']:
        if queue:
            print(queue[-1])
        else:
            print(-1)
