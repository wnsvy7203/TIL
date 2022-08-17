'''
visited[], stack[] 초기화
DFS(v)
    시작점 v 방문
    visited[v] <- True
    while
        if (v의 인접 정점 중 방문 안 한 정점 w가 있으면)
            push(v)
            v <- w (w 방문)
            visited[w] <- True
        else
            if (스택이 비어 있지 않으면)
                v <- pop(stack)
            else
                break
'''

adjList = [[1, 2],      # 0
           [0, 3, 4],   # 1
           [0, 4],      # 2
           [1, 5],      # 3
           [1, 2, 5],   # 4
           [3, 4, 6],   # 5
           [5]]         # 6

# 간선 = edge
def dfs(v):
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


N = 7
visited = [0] * N
stack = [0] * N
dfs(1)