def dfs(r, c):
    global res

    if arr[r][c] == 3:
        res = 1

    stk.append((r, c))

    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]

        if (0 <= nr < N and 0 <= nc < N and (arr[nr][nc] == 0 or arr[nr][nc] == 3)) and (nr, nc) not in stk:
            dfs(nr, nc)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    res = 0
    stk = []

    r = c = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                r = i
                c = j

    dfs(r, c)
    print(f'#{tc} {res}')
