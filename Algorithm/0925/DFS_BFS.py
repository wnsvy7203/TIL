import sys


def dfs(v):
    visited = [0 for _ in range(N+1)]
    visited[v] = 1
    top = -1
    dfs_list = [v]

    stk = [0 for _ in range(N+1)]
    while True:
        for w in adjList[v]:
            if not visited[w]:
                top += 1
                stk[top] = v
                visited[w] = 1
                dfs_list.append(w)
                v = w
                break
        else:
            while top > -1:
                v = stk[top]
                top -= 1
            if top == -1:
                break

    return dfs_list


def bfs(root):
    visited = [0 for _ in range(N+1)]
    visited[root] = 1

    bfs_list = [root]

    queue = [root]
    while queue:
        v = queue.pop(0)
        for w in adjList[v]:
            if not visited[w]:
                visited[w] = 1
                queue.append(w)
                bfs_list.append(w)

    return bfs_list


N, M, V = map(int, sys.stdin.readline().split())
Edge = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
adjList = [[] for _ in range(N + 1)]

for i in range(M):
    adjList[Edge[i][0]].append(Edge[i][1])
    adjList[Edge[i][1]].append(Edge[i][0])

for i in adjList:
    i.sort()


print(*dfs(V))
print(*bfs(V))
