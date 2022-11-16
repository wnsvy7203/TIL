import sys

N, K = map(int, sys.stdin.readline().split())

dp = [0 for _ in range(100001)]
val = []

for _ in range(N):
    val.append(tuple(map(int, sys.stdin.readline().split())))

val.sort()

for i in range(K):

