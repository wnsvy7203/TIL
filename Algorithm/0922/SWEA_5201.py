# D3
# 135ms

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))     # 무게
    t = list(map(int, input().split()))     # 트럭

    w.sort(reverse=True)
    t.sort(reverse=True)

    total = 0                               # 무게 총합
    for i in range(N):
        for j in range(M):
            if w[i] <= t[j]:                # 뒤에서부터 무게가 맞으면
                total += w[i]               # total 에 더하고
                w[i] = 0                    # 사용한 무게와 트럭은 0으로 초기화
                t[j] = 0
                break                       # 더 탐색하지 않도록 break

    print(f'#{tc} {total}')
