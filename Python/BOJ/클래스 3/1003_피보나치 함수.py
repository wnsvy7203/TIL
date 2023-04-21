# silver 3
# 68ms

import sys


# def fibonacci(n):
#     global cnt0, cnt1
#     if n == 0:
#         cnt0 += 1
#     elif n == 1:
#         cnt1 += 1
#     else:
#         fibonacci(n-1) + fibonacci(n-2)
#
#     return cnt0, cnt1


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    cnt0 = [1, 0]       # 0의 개수
    cnt1 = [0, 1]       # 1의 개수

    for i in range(N+1):
        if i == 0 or i == 1:
            continue
        cnt0.append(cnt0[-2] + cnt0[-1])
        cnt1.append(cnt1[-2] + cnt1[-1])

    print(f'{cnt0[N]} {cnt1[N]}')

    # f_stack = [[0, 0]] * (N+1)
    # f_stack[0] = [1, 0]
    # if N >= 1:
    #     f_stack[1] = [0, 1]
    #     if N >= 2:
    #         for i in range(2, N+1):
    #             f_stack[i][0] = f_stack[i-1][0] + f_stack[i-2][0]
    #             f_stack[i][1] = f_stack[i-1][1] + f_stack[i-2][1]

    # print(*f_stack[N])
