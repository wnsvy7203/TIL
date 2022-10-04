# silver 4
# 120ms

import sys
N, M = map(int, input().split())

not_listen = {}                             # 리스트로 선언해서 append 하면 시간초과
for i in range(N):
    put = sys.stdin.readline().rstrip()
    not_listen[put] = i

ans = []
for _ in range(M):
    put = sys.stdin.readline().rstrip()
    if put in not_listen:
        ans.append(put)

# 'in' 연산자의 시간 복잡도
# list, tuple 평균 : O(n)
# set, dictionary 평균 : O(1)

print(len(ans))
for i in sorted(ans):
    print(i)
