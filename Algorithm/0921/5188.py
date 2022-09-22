def dfs(r, c):
    global ans, myMin           # 전역 변수 선언하지 않으면 ans 매번 초기화
    dr = [0, 1]                 # 오른쪽과 밑으로만 간다.
    dc = [1, 0]

    if myMin < ans:             # myMin 이 ans 보다 크면 이미 함수가 돌아갈 이유가 없다.
        return

    if r == N-1 and c == N-1:   # 목적지가 정해져있으므로,
        if myMin > ans:         # 목적지 도착 시,
            myMin = ans         # myMin 갱신
        return

    for d in range(2):          # dfs 구현
        nr = r + dr[d]
        nc = c + dc[d]

        if nr > N-1 or nc > N-1:
            continue

        ans += arr[nr][nc]
        dfs(nr, nc)
        ans -= arr[nr][nc]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = arr[0][0]
    myMin = 10 * N * N          # 모든 칸의 최대 수는 10이다

    dfs(0, 0)                   # 함수 호출

    print(f'#{tc} {myMin}')     # 출력
