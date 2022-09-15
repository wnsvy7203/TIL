from collections import deque
import sys

N = int(sys.stdin.readline())
arr = list(input().split() for _ in range(N))
q = deque()

for i in arr:
    if i[0] == 'push_front':
        q.appendleft(i[1])
    elif i[0] == 'push_back':
        q.append(i[1])
    elif i[0] == 'pop_front':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif i[0] == 'pop_back':
        if q:
            print(q.pop())
        else:
            print(-1)

    if i == ['size']:
        print(len(q))
    elif i == ['empty']:
        if q:
            print(0)
        else:
            print(1)
    elif i == ['front']:
        if q:
            print(q[0])
        else:
            print(-1)
    elif i == ['back']:
        if q:
            print(q[-1])
        else:
            print(-1)
