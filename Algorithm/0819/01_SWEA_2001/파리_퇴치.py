# 149ms
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0                        # 최다킬 초기화

    for i in range(N-M+1):
        for j in range(N-M+1):          # 출발점 설정
            kill = 0                    # 죽인 파리 수 초기화
            for a in range(i, i+M):     # 출발점에서부터 M*M만큼 죽인 파리를 더한다.
                for b in range(j, j+M):
                    kill += arr[a][b]
            if max_kill < kill:         # 최댓값 갱신
                max_kill = kill

    print(f'#{tc} {max_kill}')
