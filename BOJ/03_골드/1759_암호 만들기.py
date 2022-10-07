# gold 5
# 68ms

import sys
from itertools import combinations

L, C = map(int, sys.stdin.readline().split())
words = sorted(sys.stdin.readline().split())
vowels = {'a', 'e', 'i', 'o', 'u'}

for i in combinations(words, L):
    string = ''
    for j in range(L):
        string += i[j]

    cnt = len(set(string) - vowels)
    if 2 <= cnt != L:
        print(string)
