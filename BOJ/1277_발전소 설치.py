import sys

N, W = map(int, sys.stdin.readline())
M = float(sys.stdin.readline())

graph = [[] for _ in range(N)]

for _ in range(N):


for _ in range(W):
    X, Y = map(int, sys.stdin.readline())
    graph[X].append(Y)
    graph[Y].append(X)

