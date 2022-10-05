# silver 4
# 260ms

import sys

N, M = map(int, sys.stdin.readline().split())
txt = {}

for _ in range(N):
    site, pwd = sys.stdin.readline().split()
    txt[site] = pwd

for _ in range(M):
    print(txt[sys.stdin.readline().rstrip()])
