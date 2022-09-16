# D4


def dfs(r, c):
    visited = [[0] * N for _ in range(N)]
    visited[r][c] = 1
    cnt = 0
    value = 0

    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    for r in range(N):
        for c in range(N):
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 > nr or nr >= N or 0 > nc or nc >= N:
                    continue

                if visited[nr][nc] == 0 and arr[r][c] + 1 == arr[nr][nc]:
                    visited[nr][nc] = visited[r][c] + 1
                    if cnt < visited[nr][nc]:
                        cnt = visited[nr][nc]
                        value = arr[nr][nc]
                    bfs(nr, nc)

    return [value, cnt]


T = int(input())

for x in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    stack = []

    for i in range(N):
        for j in range(N):
            stack.append((i, j))
    result.sort()

    print(f'#{x} {result[-1][0]} {result[-1][1]}')
