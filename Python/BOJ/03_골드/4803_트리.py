# gold 4
# 2980ms

import sys


def find_tree(x):
    flag = True

    stk = [x]
    while stk:
        v = stk.pop()

        if visited[v]:
            flag = False

        visited[v] = 1
        for w in graph[v]:
            if not visited[w]:
                stk.append(w)

    return int(flag)


tc = 0
while True:
    tc += 1
    n, m = map(int, sys.stdin.readline().split())

    if n == 0 and m == 0:
        break

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0 for _ in range(n+1)]

    T = 0
    for i in range(1, n+1):
        if not visited[i]:
            T += find_tree(i)

    if T == 0:
        print(f'Case {tc}: No trees.')
    elif T == 1:
        print(f'Case {tc}: There is one tree.')
    elif T > 1:
        print(f'Case {tc}: A forest of {T} trees.')
