# 142ms

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    ch1 = [0] * (N + 1)                         # 각 노드에 연결된 왼쪽 자식 노드 확인
    ch2 = [0] * (N + 1)                         # 각 노드에 연결된 오른쪽 자식 노드 확인

    calc = [0] * (N + 1)                        # 계산

    for i in range(1, (N//2)+1):
        ch1[i] = i * 2                          # 왼쪽 노드는 반드시 있다.
        if i * 2 + 1 <= N:                      # 오른쪽 노드는 있을 수도 있고, 없을 수도 있으므로 인덱스 에러 방지
            ch2[i] = i * 2 + 1

    for i in range(M):
        calc[arr[i][0]] = arr[i][1]             # 리프 노드의 값 갱신

    for i in range(N//2, 0, -1):                # 리프 노드를 제외하고 뒤에서부터 거슬러 올라온다.
        if i * 2 + 1 <= N:                      # 인덱스 에러 방지
            calc[i] = calc[i*2] + calc[i*2+1]
        else:
            calc[i] = calc[i*2]

    print(f'#{tc} {calc[L]}')
