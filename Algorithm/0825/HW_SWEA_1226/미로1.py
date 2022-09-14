# 이전의 다른 미로 문제보다 주어진 조건도 많고, 심지어 1로 벽도 이미 둘러져 있다.


def bfs(i, j):
    queue = [(i, j)]
    visited[i][j] = 1
    while queue:
        i, j = queue.pop(0)
        if maze[i][j] == 3:
            return 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < 16 and 0 <= nj < 16:
                if maze[ni][nj] != 1 and visited[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
                    queue.append((ni, nj))
    return 0


for tc in range(1, 11):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    sti = -1
    stj = -1

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
        if sti != -1:
            break

    print(f'#{tc} {bfs(sti, stj)}')

