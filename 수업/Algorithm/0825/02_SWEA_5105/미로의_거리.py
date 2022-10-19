def dfs(i, j, s, N):                                            # i, j = 배열 중 2의 좌표
    global minV                                                 # s = 움직인 거리
    if maze[i][j] == 3:                                         # maze[i][j] = 3일 경우에만 s로 바꿔준다.
        minV = s
        return
    else:
        visited[i][j] = 1                                       # 방문 표시
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:       # 방향 설정
            ni, nj = i + di, j + dj                             # 다음 갈 곳 설정
            if 0 <= ni < N and 0 <= nj < N:                     # 인덱스 에러 방지
                if maze[ni][nj] != 1 and visited[ni][nj] == 0:  # 다음 갈 곳이 1이 아니고, 이전에 방문하지도 않은 경우
                    dfs(ni, nj, s + 1, N)                       # 반복
        visited[i][j] = 0                                       # 반복하는 경우, 방문 초기화
        return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]          # 미로 입력
    sti = -1                                                    # 2의 인덱스를 저장하기 위한 변수 초기화
    stj = -1

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sti, stj = i, j
                break
        if sti != -1:
            break

    minV = 0                                                    # 최단거리 저장
    visited = [[0] * N for _ in range(N)]                       # 방문 여부를 묻는 변수 저장
    dfs(sti, stj, -1, N)                                        # 최초 방문한 곳은 -1부터 시작
    print(f'#{tc} {minV}')

