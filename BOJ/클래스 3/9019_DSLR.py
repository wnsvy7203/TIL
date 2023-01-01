# gold 4
# pypy3 기준 6212ms

# D: D 는 n을 두 배로 바꾼다. 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다.
# 그 결과 값(2n mod 10000)을 레지스터에 저장한다.
# S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다.
# n이 0 이라면 9999 가 대신 레지스터에 저장된다.
# L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다.
# 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다.
# R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다.
# 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.

import sys
from collections import deque


def bfs():
    while que:
        res, ans = que.popleft()
        visited[res] = 1
        if res == B:
            return ans

        res_d = 2 * res % 10000
        if not visited[res_d]:
            que.append((res_d, ans+'D'))
            visited[res_d] = 1

        if res == 0:
            res_s = 9999
        else:
            res_s = res - 1
        if not visited[res_s]:
            que.append((res_s, ans+'S'))
            visited[res_s] = 1

        res_l = (10 * res + (res // 1000)) % 10000
        if not visited[res_l]:
            que.append((res_l, ans+'L'))
            visited[res_l] = 1

        res_r = (res % 10) * 1000 + res // 10
        if not visited[res_r]:
            que.append((res_r, ans+'R'))


T = int(sys.stdin.readline())
for _ in range(T):
    visited = [0 for _ in range(10000)]

    A, B = map(int, sys.stdin.readline().split())
    que = deque([(A, '')])
    print(bfs())
