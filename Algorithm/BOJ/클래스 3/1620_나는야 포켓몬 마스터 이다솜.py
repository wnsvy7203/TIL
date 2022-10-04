# silver 4
# 272ms

import sys

N, M = map(int, sys.stdin.readline().split())
poke = {}

for i in range(1, N+1):
    poke[i] = sys.stdin.readline().rstrip()

poke_rev = {v: idx for idx, v in poke.items()}

for _ in range(M):
    find = sys.stdin.readline().rstrip()
    if find.isdigit():
        print(poke.get(int(find)))
    else:
        print(poke_rev.get(find))
