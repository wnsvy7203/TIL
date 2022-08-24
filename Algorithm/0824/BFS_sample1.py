import sys
sys.stdin = open('input.txt')

def make_graph(graph, data):
    for i in range(0, len(data), 2):
        v1, v2 = data[i], data[i+1]
        if v1 in graph.keys():
            graph[v1].append(v2)
        else:
            graph[v1] =  [v2]

        if v2 in graph.keys():
            graph[v2].append(v1)
        else:
            graph[v2] = [v1]


def BFS(node, q, visited, graph):
    q.append(node)
    if node not in visited:
        visited.append(node)

    while q:
        node = q.popleft()
        for e in graph[node]:
            if e not in visited:
                visited.append(e)
                q.append(e)


v, e = input().split()
data = input().split()
visited = []

from collections import defaultdict, deque

graph = defaultdict(list)
q = deque()

make_graph(graph, data)

BFS("1", q, visited, graph)
print(visited)
