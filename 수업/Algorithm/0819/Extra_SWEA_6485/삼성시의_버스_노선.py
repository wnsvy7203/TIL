# 152ms

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    bus_stop = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    C = []
    for _ in range(P):
        a = int(input())
        C.append(a)

    road = [0] * 5001               # 5000개의 정류장, 인덱스 0은 버린다.

    for i in range(N):
        A = bus_stop[i][0]
        B = bus_stop[i][1]
        for j in range(A, B+1):
            road[j] += 1

    print(f'#{tc}', end=' ')
    for i in C:
        print(road[i], end=' ')
    print()

