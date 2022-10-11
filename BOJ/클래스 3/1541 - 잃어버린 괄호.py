# silver 2
# 84ms

# 가장 작은 값을 도출해야 하므로,
# 순서에 상관없이 +를 모두 먼저 수행하고 -를 수행하면 최소가 된다.

import sys
from collections import deque

exp = sys.stdin.readline().rstrip()         # 표현식을 먼저 받는다.
mid = []                                    # 중간결과를 담을 리스트 mid 선언

nums = ''                                   # 숫자를 받는다.
for i in range(len(exp)):
    if exp[i].isdigit():                    # i번 인덱스가 숫자면
        nums += exp[i]                      # 숫자에 더해주고
    else:
        mid.append(nums)                    # +나 -라면, 더해 온 nums 를 mid 에 더하고
        mid.append(exp[i])                  # +나 -도 더한다.
        nums = ''                           # nums 는 초기화
else:
    mid.append(nums)                        # for 문을 전부 돌면 마지막에 숫자가 하나 반드시 남으므로, 더해준다.

for i in range(len(mid)):                   # mid 를 전부 돌면서
    if mid[i] == '+':                       # + 면, 바로 뒤 인덱스에는 앞의 숫자와 뒤의 숫자를 더해서 넣고,
        mid[i+1] = str(int(mid[i-1]) + int(mid[i+1]))
        mid[i-1] = '0'                      # - 면, 바로 앞 인덱스에는 0을 넣어준다.

# 이후로는 후위표기법에 따라 계산만 해주면 된다.

res = deque()
cal = []
for i in range(len(mid)):
    if mid[i].isdigit() and mid[i] != '0':
        res.append(int(mid[i]))
    elif mid[i] == '-':
        cal.append(mid[i])

while cal:
    cal.pop()
    a = res.popleft()
    b = res.popleft()

    res.appendleft(a - b)

print(res[-1])
