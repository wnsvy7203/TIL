def dfs(v):
    print(v, end=' ')
    visited[v] = 1

    for w in adjM[v]:
        if not visited[w]:
            dfs(w)


arr = list(map(int, input().split()))
N = len(arr)
M = len(arr) // 2
adjM = [[] for _ in range(M+1)]
visited = [0] * (M+1)

for i in range(0, N, 2):
    adjM[arr[i]].append(arr[i+1])
    adjM[arr[i+1]].append(arr[i])


dfs(1)
print()
