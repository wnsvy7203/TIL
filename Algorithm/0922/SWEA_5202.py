# D3
# 156ms

from collections import deque

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    time = sorted([list(map(int, input().split())) for _ in range(N)])
    time.sort(key=lambda x: x[1])
    time = deque(time)

    res = [time.popleft()]

    while time:
        home = res[-1][1]
        next_truck = time.popleft()
        next_start = next_truck[0]

        if home <= next_start:
            res.append(next_truck)

    print(f'#{tc} {len(res)}')
