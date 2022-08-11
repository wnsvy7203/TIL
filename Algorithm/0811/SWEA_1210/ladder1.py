import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    r, c = 99, 0 # arr[r][c] = 2인 값의 인덱스를 받을 변수
    d = 0 # 방향을 정할 d
    row = [-1, 0, 0] # 아래로는 갈 일이 없으니까,
    col = [0, -1, 1] # 위, 왼쪽, 오른쪽만 찾으면 되겠다.

    for i in range(100):
        if arr[99][i] == 2:
            c = i # arr[i][j]가 2인 인덱스 저장

    while r:
        if d == 0:
            if c != 0:
                if arr[r][c-1] == 1:
                    d = 1
            if c != 99:
                if arr[r][c+1] == 1:
                    d = 2 # 위로 갈 때는 반드시 왼쪽이나 오른쪽에 1이 있으면 그 방향으로 꺾어야 한다.

        else:
            if 0 <= r+row[d] <= 99 and 0 <= c+col[d] <= 99:
                if arr[r+row[d]][c+col[d]] == 0: # 위로 가는 게 아니라면, 직진만 계속 하다가
                                                 # 다음 값이 0일 경우 반드시 '위'로 꺾어야 한다.
                    d = 0
            else: # 인덱스 에러 방지
                d = 0

        r += row[d]
        c += col[d]

    print(f'#{tc} {c}')