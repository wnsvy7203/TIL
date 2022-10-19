def f(i, N):        # i: 현재 단계, N: 목표 단계
    if i == N:
        print(i)
        return
    else:
        print(i)
        f(i+1, N)


f(0, 3)
