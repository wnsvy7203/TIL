T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di1 = [0, 1, 0, -1]                                 # 우, 하, 좌, 상
    dj1 = [1, 0, -1, 0]

    di2 = [1, 1, -1, -1]                                # x 모양
    dj2 = [1, -1, -1, 1]

    maxV = 0                                            # 최댓값 초기화
    for i in range(N):
        for j in range(N):
            cnt1 = arr[i][j]                            # + 모양 먼저
            for k in range(4):
                for z in range(1, M):
                    ni, nj = i+di1[k]*z, j+dj1[k]*z     # 델타에 따라 이동
                    if 0 <= ni < N and 0 <= nj < N:     # 인덱스에러 방지
                        cnt1 += arr[ni][nj]             # cnt1 초기화
            if maxV < cnt1:
                maxV = cnt1                             # maxV 최신화

            cnt2 = arr[i][j]                            # x 모양
            for k in range(4):                          # 같은 과정 반복
                for z in range(1, M):
                    ni, nj = i+di2[k]*z, j+dj2[k]*z
                    if 0 <= ni < N and 0 <= nj < N:
                        cnt2 += arr[ni][nj]
            if maxV < cnt2:
                maxV = cnt2
    print(f'#{tc} {maxV}')
