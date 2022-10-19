from collections import deque

for test_case in range(1, int(input())+1):
    N, M = map(int, input().split())

    q = deque([(N, 0)])
    visited = set()
    visited.add(N)

    while q:
        n, cnt = q.popleft()
        if n == M:
            break

        if n + 1 not in visited and n + 1 <= 1000000:
            q.append((n + 1, cnt + 1))
            visited.add(n + 1)
        if n - 1 not in visited and n - 1 <= 1000000:
            q.append((n-1, cnt + 1))
            visited.add(n-1)
        if n * 2 not in visited and n * 2 <= 1000000:
            q.append((n*2, cnt + 1))
            visited.add(n*2)
        if n - 10 not in visited and n - 10 <= 1000000:
            q.append((n-10, cnt+1))
            visited.add(n - 10)

    print(f'#{test_case} {cnt}')
