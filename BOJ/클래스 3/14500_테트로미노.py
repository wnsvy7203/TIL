# gold 4
# 172ms

import sys


def dfs(r, c, cnt, res):
    # ans 로 값을 계속 갱신한다.
    global ans

    # 중간값 res 에 check(nums 중 최댓값)를 남은 횟수만큼 더해도,
    # ans 보다 작으면 작업을 계속 할 이유가 없다(백트래킹).
    if res + (check * (4 - cnt)) <= ans:
        return

    if cnt == 4:
        ans = max(ans, res)
        return

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            # 이 작업이 필요한 이유는
            # T-테트리미노의 경우에는 일반적인 dfs 사용 시 나오지 않는 모양
            # 2번째를 마친 후, 자기 자신에서 출발하는 새로운 dfs 가 필요
            if cnt == 2:
                visited[nr][nc] = 1
                dfs(r, c, cnt+1, res+nums[nr][nc])
                visited[nr][nc] = 0

            visited[nr][nc] = 1
            dfs(nr, nc, cnt+1, res+nums[nr][nc])
            visited[nr][nc] = 0


N, M = map(int, sys.stdin.readline().split())
nums = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# 2차원 배열 최댓값 찾기
check = max(map(max, nums))
visited = [[0] * M for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

ans = 0

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, nums[i][j])
        visited[i][j] = 0

print(ans)
