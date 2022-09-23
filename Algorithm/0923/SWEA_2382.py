# 3379ms

T = int(input())

for x in range(1, T+1):
    N, M, K = map(int, input().split())
    micro = [list(map(int, input().split())) for _ in range(K)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for _ in range(M):
        for mi in micro:
            mi[0] += dr[mi[3]-1]                                            # 인덱스 에러에 유의하세요
            mi[1] += dc[mi[3]-1]

            if mi[0] == 0 or mi[1] == 0 or mi[0] == N-1 or mi[1] == N-1:    # 끝에 도달하면,
                mi[2] //= 2                                                 # 2로 나눠준다.
                if mi[3] % 2:                                               # 상, 좌인 경우
                    mi[3] += 1                                              # 하, 우로 바꿔
                else:                                                       # 반대의 경우도
                    mi[3] -= 1                                              # 업데이트

        micro.sort()                                                        # 정렬
        # print(micro)

        # 일반 sort 를 사용했기 때문에, 같은 좌표일 경우, 반드시 미생물의 수가 많은 군집이 뒤로 가게 되어 있다.
        for i in range(K-1, -1, -1):                                        # 따라서, 뒤에서부터 탐색
            if micro[i][2] == 0:                                            # 미생물이 없으면 탐색 불필요
                continue

            for j in range(1, i+1):
                if micro[i][0] == micro[i-j][0] and micro[i][1] == micro[i-j][1]:
                    micro[i][2] += micro[i-j][2]                            # 같으면 뺏어오고,
                    micro[i-j][2] = 0                                       # 뺏긴 애는 0 처리
                else:
                    break                                                   # 더 이상 같지 않으면 break 로 탐색 종료

    res = 0
    for mi in micro:
        res += mi[2]                                                        # res 에 모두 담아서

    print(f'#{x} {res}')                                                    # 출력
