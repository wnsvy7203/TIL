def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x


def union(x, y):
    rep[find_set(y)] = find_set(x)


V, E = map(int, input().split())    # V 마지막 정점, 0~V번 정점. 개수 (V+1)개
edge = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append([w, v, u])
edge.sort()
rep = [i for i in range(V+1)]       # 대표원소 배열
# MST 의 간선수 = 정점 수 - 1
N = V + 1   # 정점 수
cnt = 0     # 선택한 edge 의 수
total = 0   # MST 가중치의 합
for w, v, u in edge:
    if find_set(v) != find_set(u):
        cnt += 1
        union(u, v)
        total += w
        if cnt == N-1:  # MST 구성이 끝나면
            break
print(total)
