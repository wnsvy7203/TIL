# 252ms 돌리는 건 큰 차이가 없네

for tc in range(1, 11):
    N = int(input())    # 항상 100이래
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0                                                 # 교착 상태 개수를 세자.
    # for i in range(N):
    #     for j in range(i):
    #         arr[i][j], arr[j][i] = arr[j][i], arr[i][j]   # 계산의 편의를 위해 가로 세로를 돌려보자.

    i = 0
    while i < N:                                            # 돌렸으니까, 가로로만 생각하면 된다.
        for j in range(N):
            if arr[j][i] == 1:                              # 1이 나오면 시작
                for k in range(j+1, N):                     # 1이 나온 다음부터 계속 돌아간다.
                    if arr[k][i] == 1:                      # 1 다음 1이 나오면, 의미 없으므로
                        break                               # 반복문 탈출
                    elif arr[k][i] == 2:                    # 1 다음 나오는 숫자가 2이면
                        cnt += 1                            # cnt 에 1 더하고
                        break                               # 다음 1을 찾으러 탈출
        i += 1

    print(f'#{tc} {cnt}')
