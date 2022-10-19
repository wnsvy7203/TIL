# D3
# 220ms

def dfs(v):
    global cnt
    if v == N:
        cnt += 1
        return
    else:
        for i in range(N):
            visited[v] = i
            flag = True
            for j in range(v):
                if visited[v] == visited[j] or abs(visited[v] - visited[j]) == abs(v - j):
                    flag = False

            if flag:
                dfs(v+1)


T = int(input())

for x in range(1, T+1):
    N = int(input())
    cnt = 0
    visited = [0] * N
    dfs(0)

    print(f'#{x} {cnt}')
