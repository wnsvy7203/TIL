from itertools import permutations
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline()))

for perm in permutations(A, N):
    for i in range(N):
        pass