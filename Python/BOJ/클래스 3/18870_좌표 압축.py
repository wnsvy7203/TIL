# silver 2
# 1900ms
# list.index 빅O notation 은 O(1)인데 왜 시간 초과가 나는지 모르겠다.

import sys

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))
Xi = sorted(list(set(X)))
cnt = {Xi[i]: i for i in range(len(Xi))}

for i in X:
    print(cnt[i], end=' ')
