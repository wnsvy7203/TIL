# 128ms

T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())
    change = [list(map(int, input().split())) for _ in range(Q)]

    box = [0] * N                   # 내부가 모두 0으로 초기화된 box 정의

    for i in range(Q):
        L = change[i][0]            # L은 왼쪽 변수
        R = change[i][1]            # R은 오른쪽 변수
        for j in range(L, R+1):     # L ~ R 까지 바꿔야하므로,
            box[j-1] = i+1          # 인덱스를 맞춰주고 바꾼다.

    print(f'#{tc}', *box)
