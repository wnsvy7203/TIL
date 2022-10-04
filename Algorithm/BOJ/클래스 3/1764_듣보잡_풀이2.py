# silver 4
# 120ms

import sys
N, M = map(int, input().split())

not_listen = [sys.stdin.readline().rstrip() for _ in range(N)]                            # 리스트로 선언해서 append 하면 시간초과
not_see = [sys.stdin.readline().rstrip() for _ in range(M)]

no = list(set(not_listen) & set(not_see))

print(len(no))
for ans in sorted(no):
    print(ans)

# set 은 수학에서의 집합과 같다. 따라서, 논리 연산자를 모두 사용할 수 있다.
# 논리 연산자
# 1. 합집합: A | B == A.union(B)
# 2. 교집합: A & B == A.intersection(B)
# 3. 차집합: A - B == A.difference(B)
