T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    # K: 1회 충전으로 이동할 정류장 수
    # N: N 번까지 이동
    # M: 충전기가 설치된 정류장 개수
    center = list(map(int, input().split()))

    arr = [0] * (N+1)               # N 까지의 정류장

    for i in center:
        for j in range(N+1):
            if j == i:
                arr[j] = 1          # 충전기가 설치된 정류장을 1, 설치되지 않은 정류장은 0
    bus = 0                         # 버스의 현재 위치를 나타내는 변수
    cnt = 0                         # 충전 횟수
    while True:
        for i in range(K, 0, -1):   # K부터 내려오면서
            if arr[i] == 1:         # 1이 있으면
                cnt += 1            # 충전하고
                arr = arr[i:]       # 리스트 슬라이싱
                bus += i            # 충전하면 버스의 현재 위치 업데이트
                break               # 리스트 슬라이싱 했으면 처음으로 돌아간다.
        if bus + K >= N:
            break                   # 반복하다가 bus 의 현재 위치가 N보다 뒤에 있으면 마무리
                                    # 범위 내에 0밖에 없을 때,
        if 1 not in arr[K:0:-1]:    # 구간 내에 1이 없으면 cnt 값 초기화하고 반복문 탈출
            cnt = 0
            break

    print(f'#{tc} {cnt}')
