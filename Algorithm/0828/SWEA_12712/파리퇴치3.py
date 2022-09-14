T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(N)]

    kill_stack = []
    for i in range(N):
        for j in range(N):
            kill = kill2 = fly[i][j]
            for k in range(1, M):
                if i+k < N:
                    kill += fly[i+k][j]
                    if j+k < N:
                        kill2 += fly[i+k][j+k]
                    if j-k >= 0:
                        kill2 += fly[i+k][j-k]
                if j+k < N:
                    kill += fly[i][j+k]
                if i-k >= 0:
                    kill += fly[i-k][j]
                    if j-k >= 0:
                        kill2 += fly[i-k][j-k]
                    if j+k < N:
                        kill2 += fly[i-k][j+k]
                if j-k >= 0:
                    kill += fly[i][j-k]
            kill_stack.append(kill)
            kill_stack.append(kill2)
    print(f'#{tc} {max(kill_stack)}')
