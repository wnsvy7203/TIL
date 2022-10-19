'''
0번부터 V번까지, E개의 간선
6 8 (V E) 총 7개
0 1
0 2
1 3
1 4
2 4
3 5
4 5
5 6
'''

def dfs(v):
    print(v)
    top = -1

    visited[v] = 1      # 시작점 방문 표시
    while True:
        for w in adjList[v]: # v의 인접 정점 중 방문 안 한 정점 w가 있으면
            if visited[w] == 0:
                top += 1     # push(v)
                stack[top] = v
                v = w        # w 방문
                print(v)     # 방문 확인
                visited[w] = 1
                break
        else:                # w가 없으면
            if top != -1:
                v = stack[top]
                top -= 1
            else:
                break

V, E = map(int, input().split())
N = V + 1
adjList = [[] for _ in range(N)]
for _ in range(E):
    a, b = map(int, input().split())
    adjList[a].append(b)
    adjList[b].append(a)

visited = [0] * N
stack = [0] * N

dfs(1)