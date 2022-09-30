# silver 4
# pypy 로만 제출 가능 - 29404ms

import sys


def flag(v):
    for i in range(v):
        if visited[v] == visited[i] or abs(visited[v] - visited[i]) == abs(v - i):
            return False
    return True


def dfs(v):
    global cnt
    if v == N:
        cnt += 1
        return
    else:
        for i in range(N):
            visited[v] = i

            if flag(v):
                dfs(v+1)


N = int(sys.stdin.readline())
cnt = 0
visited = [0] * N
dfs(0)

print(cnt)
