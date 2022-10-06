import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    cloth = {}

    for _ in range(N):
        name, kind = sys.stdin.readline().split()
        cloth[kind] += name

