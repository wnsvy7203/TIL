# silver 3
# 88ms

# 딕셔너리에 저장
# 종류를 최소 1개 선택하고, 종류별로 최대 1개씩의 옷을 선택하는 경우의 수 출력
# 종류별로 선택을 하는 경우의 수
# 선택을 하는 경우도 한 가지, 선택을 하지 않는 경우도 한 가지
# defaultdict 선언해서 초깃값을 1로 설정하면, 선택을 하지 않는 경우는 고려하지 않아도 된다.

import sys
from collections import defaultdict

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    cloth = defaultdict(lambda: 1)                  # 초깃값 설정하는 방법

    for _ in range(N):
        name, kind = sys.stdin.readline().split()   # 종류의 개수만 세면 된다.
        cloth[kind] += 1

    cnt = 1
    for i in cloth:
        cnt *= cloth[i]

    print(cnt-1)                                    # 아무 종류도 선택하지 않은 경우는 빼 줘야 한다.
