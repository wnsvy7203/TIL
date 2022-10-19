from collections import deque

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    new_C = []                                  # enumerate 한 C를 받을 리스트 new_C
    for idx, num in enumerate(C, start=1):      # idx, num 을 한꺼번에 new_C 에 추가
        new_C.append([idx, num])

    piz = deque()                               # 오븐을 deque 로 저장
    for i in range(N):                          # piz 는 N 만큼의 길이를 가진다.
        piz.append(new_C[i])

    n = N                                       # n을 N으로 초기화
    while len(piz) > 1:                         # 1이 되면 출력하면 된다.
        piz[0][1] //= 2                         # enumerate 한 값 중 치즈의 값만 계속 // 2 한다.
        if piz[0][1] == 0:                      # 0이 됐을 경우
            piz.popleft()                       # 왼쪽에서 빼고
            if n < M:                           # n < M 이라면
                piz.appendleft(new_C[n])        # new_C에서 새로운 값을 불러온다.
                n += 1                          # n 을 더해준다.
            else:                               # n >= M 이라면
                continue                        # new_C에 값이 없으므로, continue
        piz.rotate(-1)                          # 작업을 마무리하면 방향을 돌려준다.
    print(f'#{tc} {piz[0][0]}')                 # 하나 남은 값의 인덱스 값을 반환한다.
