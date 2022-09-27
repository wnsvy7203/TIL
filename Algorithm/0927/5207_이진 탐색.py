# D3
# 115ms

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    res = 0                                             # 결과값 갱신

    for i in B:                                         # B 의 원소 탐색
        flag = False                                    # 불리안 변수
        cnt = []                                        # 왼쪽인지 오른쪽인지 세 줄 cnt 리스트 정의
        s = 0                                           # 시작점, 마지막 점 설정
        e = N - 1
        while s <= e:                                   # 이진 탐색
            m = (s + e) // 2                            # 중간값 갱신

            if i < A[m]:                                # A의 m번째 인덱스보다 작다면
                e = m - 1                               # e 갱신
                cnt.append(1)                           # 왼쪽을 탐색한다는 의미에서 1 append
            elif i > A[m]:                              # A의 m번째 인덱스보다 크다면
                s = m + 1                               # s 갱신
                cnt.append(2)                           # 오른쪽을 탐색한다는 의미에서 2 append
            else:
                flag = True                             # 값을 찾았다는 의미이므로, flag 를 True 로 변경
                break

        if flag:                                        # i가 A 안에 있을 경우에, 즉, flag 가 True 일 때만 고려한다.
            if len(cnt) < 2:                            # cnt 의 길이가 2보다 작은 경우에는 res 추가
                res += 1
            elif len(cnt) >= 2:                         # cnt 의 길이가 2보다 큰 경우에는
                for idx in range(len(cnt) - 1):         # 반복문을 돌면서 모든 경우에 앞 뒤가 달라야 하므로,
                    if cnt[idx] == cnt[idx+1]:          # 같다면
                        break                           # break
                else:
                    res += 1                            # break 없이 모든 for 문을 탐색했다면, res 추가

    print(f'#{tc} {res}')
