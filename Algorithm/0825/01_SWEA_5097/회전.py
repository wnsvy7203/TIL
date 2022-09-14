# 132ms

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(M):                      # M번 하세요
        a = arr.pop(0)                      # 앞에 거 빼고
        arr.append(a)                       # 뺀 거 다시 넣으세요

    print(f'#{tc} {arr.pop(0)}')            # 앞에 거 빼서 출력하세요
