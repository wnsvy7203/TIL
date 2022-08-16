T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 10 <= N <= 100, 5 <= M <= N
    arr = [list(map(str, input())) for _ in range(N)]

    # N * N 크기의 글자판에서 길이가 M인 회문
    # 회문은 하나밖에 없다.
    # 세로도 가능
    # 1. 가로줄
    for i in range(N):
        new_arr = []
        for j in range(N-M+1):
            for k in range(j, j+M):
                new_arr.append(arr[i][k])
        if new_arr == new_arr[::-1]:
            print(f'#{tc}', *new_arr)
            break

    for i in range(N):
        for j in range(i):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    # 2. 세로줄
    for i in range(N):
        new_arr = []
        for j in range(N-M+1):
            for k in range(j, j+M):
                new_arr.append(arr[i][k])
        if new_arr == new_arr[::-1]:
            print(f'#{tc}', *new_arr)
            break
