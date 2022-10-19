
T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())         # N: 손님 수, M: 단위 초, K: 나오는 붕어빵 개수
    cus = list(map(int, input().split()))       # cus: 손님 몇 초에 오지?
    cus.sort()                                  # 정렬

    for i in range(N):
        if cus[i] < M:                          # 손님이 한 명이라도 M초 전에 오면 어차피 실패
            print(f'#{tc} Impossible')
            break
        else:
            if N <= K:                            # 오는 손님보다 단위 초에 나오는 붕어빵 수가 더 많으면
                print(f'#{tc} Possible')          # 반드시 성공
                break
    else:
        flag = True
        cnt = 0                                 # 현재 붕어빵 개수
        for a in range(1, max(cus)+1):          # 지금 몇 초?
            if a % M == 0:                      # 단위 초의 배수면, 붕어빵이 나오므로
                cnt += K                        # 붕어빵을 더해준다.
            for b in range(len(cus)):
                cus[b] -= 1
                if cus[b] == 0:
                    cnt -= 1                    # 붕어빵 내 주고 현재 개수 업데이트
                    if cnt == -1:
                        flag = False
                        break
                    continue                   # 1초씩 줄여준다.
        if flag:
            print(f'#{tc} Possible')
        else:
            print(f'#{tc} Impossible')
