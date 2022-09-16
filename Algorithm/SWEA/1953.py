direction = {
    1: ((-1, 0), (1, 0), (0, -1), (0, 1)),
    2: ((-1, 0), (1, 0)),
    3: ((0, -1), (0, 1)),
    4: ((-1, 0), (0, 1)),
    5: ((1, 0), (0, 1)),
    6: ((0, 1), (-1, 0)),
    7: ((-1, 0), (0, -1))
}

connect = {
    1: (1, 2, 3, 4, 5, 6, 7),
    2: (1, 2, 4, 5, 6, 7),
    3: (1, 3, 4, 5, 6, 7),
    4: ()
    5: ()
    6: ()
    7: ()
}


def bfs(r, c):
    queue = [(r, c)]
    visited[r][c] = 0
    while queue:
        if d == L:
            break

        r, c = queue.pop(0)
        if pipe[r][c] in [1, 2, 4, 7]:
            if r-1 >= 0:    # 상
                nr = r - 1
                nc = c
                if pipe[nr][nc] in [1, 2, 5, 6] and visited[nr][nc] == -1:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr, nc))

        if pipe[r][c] in [1, 2, 5, 6]:
            if r+1 < N:     # 하
                nr = r + 1
                nc = c
                if pipe[nr][nc] in [1, 2, 4, 7] and visited[nr][nc] == -1:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr, nc))

        if pipe[r][c] in [1, 3, 6, 7]:
            if c-1 >= 0:    # 좌
                nr = r
                nc = c - 1
                if pipe[nr][nc] in [1, 3, 4, 5] and visited[nr][nc] == -1:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr, nc))

        if pipe[r][c] in [1, 3, 4, 5]:
            if c+1 < M:     # 우
                nr = r
                nc = c + 1
                if pipe[nr][nc] in [1, 3, 6, 7] and visited[nr][nc] == -1:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr, nc))
        d += 1

    value = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] != -1:
                value += 1
    return value


T = int(input())

for x in range(1, T+1):
    # N * M 배열
    # R, C: 맨홀 뚜껑 위치
    # L: 시간

    N, M, R, C, L = map(int, input().split())
    pipe = [list(map(int, input().split())) for _ in range(N)]
    visited = [[-1] * M for _ in range(N)]

    print(f'#{x} {bfs(R, C)}')
