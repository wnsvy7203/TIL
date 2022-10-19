T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0                                                     # 경우의 수를 세 보자

    new_arr = [[0] * (N+2) for _ in range(N+2)]                 # 인덱스 에러 방지용 0을 테두리에 씌워준다.
    for i in range(1, N+1):
        for j in range(1, N+1):
            new_arr[i][j] = arr[i-1][j-1]

    for i in range(1, N+1):
        for j in range(1, N-K+2):
            if new_arr[i][j] == 1 and new_arr[i][j-1] == 0:     # 가로 시작점 pick
                s1 = j                                          # 시작점 j를 변수 s에 저장
                for a in range(j, j+K):                         # j부터 j+K까지 돌면서
                    if new_arr[i][a] != 1:                      # 하나라도 1이 아니면
                        break                                   # 의미 없으므로 반복문 탈출
                else:
                    if new_arr[i][s1+K] == 0:                   # 반복문을 모두 돈 이후, 그 다음 인덱스 값이 0이면,
                        cnt += 1                                # cnt += 1

        for j in range(1, N-K+2):
            if new_arr[j][i] == 1 and new_arr[j-1][i] == 0:     # 세로 시작점 pick
                s2 = j                                          # 같은 과정 반복
                for a in range(j, j+K):
                    if new_arr[a][i] != 1:
                        break
                else:
                    if new_arr[s2+K][i] == 0:
                        cnt += 1

    print(f'#{tc} {cnt}')
