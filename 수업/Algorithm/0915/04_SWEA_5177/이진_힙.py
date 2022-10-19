# 149ms

import heapq

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = []

    for i in arr:
        heapq.heappush(heap, i)             # heapq 의 heappush 메소드 활용

    n = N // 2                              # 자기 자신을 제외한 조상 노드만 확인하면 되므로, n 은 N // 2로 초기화
    sum_heap = 0                            # 더한 값을 담을 sum_heap 선언
    while n:                                # n 이 0이 될 때까지 반복
        sum_heap += heap[n-1]               # heap 의 인덱스는 0부터이므로, 1씩 빼준다.
        n //= 2                             # 더한 이후에는 n을 2로 나눈다.

    print(f'#{tc} {sum_heap}')
