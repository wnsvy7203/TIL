def backtracking(y, x, ans):
    global minV

    # visited[y][x] = 1

    dy = [1, 0]     # 밑, 오른쪽
    dx = [0, 1]

    if ans >= minV:
        return

    if y == N - 1 and x == N - 1:
        minV = ans
        return

    for d in range(2):
        ny = y + dy[d]
        nx = x + dx[d]

        if ny > N - 1 or nx > N - 1:
            continue

        # if not visited[ny][nx]:
        #     visited[ny][nx] = 1
        if loc[ny][nx] - loc[y][x] > 0:
            backtracking(ny, nx, ans + (loc[ny][nx] - loc[y][x]))
        else:
            backtracking(ny, nx, ans)
            # visited[ny][nx] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    loc = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    minV = float('inf')
    backtracking(0, 0, 0)

    print(f'#{tc} {(minV + 2*(N-1))}')
