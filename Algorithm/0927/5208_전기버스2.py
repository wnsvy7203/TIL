# D3
# 116ms

T = int(input())

for tc in range(1, T+1):
    sta = list(map(int, input().split())) + [0]     # 도착점을 0으로 계속 갱신해준다.
    N = sta.pop(0)                                  # 제일 첫 번째 인덱스는 정류장의 개수를 의미한다.
    cnt = 0                                         # 교환 횟수를 셀 cnt 정의

    # station 도착점을 계속 0으로 갱신한다.
    # 정류장마다 충전하게 되면 갈 수 있는 최대 거리가 나와있으므로,
    # 앞에서부터 탐색하여 현재 위치부터 충전해서 도착지 이상 갈 수 있다면 충전해야 한다.
    # 그리고 그 위치 앞에서부터 짤라서 같은 과정 반복

    while True:                                     # station 뒤에 계속 도착점을 0으로 갱신하도록 되어 있으므로,
        for i in range(len(sta)):                   # 출발점과 도착점으로 추가될 0은 어떤 경우에도 반드시 남는다.
            if i + sta[i] >= len(sta) - 1:          # 현재 위치에서 충전해서 도착지 이상 갈 수 있다면
                cnt += 1                            # 교환 횟수 추가
                sta = sta[:i] + [0]                 # 자르고, 0 추가해준다.
                break

        if sta[0] >= len(sta) - 1:                  # 만약 처음부터 시작해서 남은 정류장을 모두 갈 수 있다면,
            break                                   # 탐색 불필요하므로 break

    print(f'#{tc} {cnt}')
