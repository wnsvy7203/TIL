T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    c = []

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt = 1
                if j+1 < M and arr[i][j+1] == 1:
                    if (j-1 >= 0 and arr[i][j-1] == 0) or (j == 0):
                        for k in range(j+1, M):
                            if arr[i][k] == 1:
                                cnt += 1
                                if k == M-1:
                                    c.append(cnt)
                            elif arr[i][k] == 0:
                                c.append(cnt)
                                break
                elif i+1 < N and arr[i+1][j] == 1:
                    if (i-1 >= 0 and arr[i-1][j] == 0) or i == 0:
                        for k in range(i+1, N):
                            if arr[k][j] == 1:
                                cnt += 1
                                if k == N-1:
                                    c.append(cnt)
                            elif arr[k][j] == 0:
                                c.append(cnt)
                                break

    print(f'#{tc} {max(c)}')
