T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)] # 가로와 세로의 길이가 N인 배열

    # 숫자가 1 커질 때마다 달팽이가 반드시 어떤 방향으로든 1칸씩 이동한다.
    d = 0 # 오른쪽부터 이동하니까, 0은 오른쪽, 1은 아래로, 2는 왼쪽, 3은 위로라고 생각한다.
    # d가 4가 되면 다시 0이 돼야 하니까 d = (d+1) % 4로 하자

    # d가 0일 때, 값이 들어갈 좌표는 [0, 0], [0, 1], [0, 2], ... [0, N-1]까지 순서대로다. -> [0, 1]만큼
    # d가 1일 때, [1, 0]
    # d가 2일 때, [0, -1]
    # d가 3일 때, [-1, 0]
    # 다 묶으면
    row = [0, 1, 0, -1]
    col = [1, 0, -1, 0]
    # [row[d], col[d]]를 각각 더해 주면 되나?

    r, c = 0, 0 # 각각 행과 열의 출발점
    s = 1 # 초기값 1

    # 첫 번째 시도에서는 arr[0][0]부터 [0][N-1]까지 총 N-1회 이동,
    # 방향을 틀면 arr[0][N-1]에서 arr[N-1][N-1]까지 총 N-2회 이동
    # 마지막까지 1씩 감소한 횟수만큼 이동, 최종적으로 이동하지 않는 건 의미가 없다.

    while s <= N ** 2: # 칸 다 채울 때까지 돌아봐
        arr[r][c] = s
        s += 1

        if (r + row[d] < 0) or (r + row[d] == N) or (c + col[d] < 0) or (c + col[d] == N) or arr[r+row[d]][c+col[d]] != 0: # 다음 위치가 인덱스를 벗어나는지 미리 확인
            d = (d+1) % 4 # 그럼 방향을 바꿔

        r += row[d]
        c += col[d]

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end = ' ')
        print()