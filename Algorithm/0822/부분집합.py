def f(i, N):
    global answer
    if i == N:
        s = 0       # 부분집합의 합
        for i in range(N):
            if bit[i]:
                s += A[i]
                # print(A[i], end=' ')
        # print()
        if s == 10:
            answer += 1     # 부분집합의 합의 10인 경우의 수
            for i in range(N):
                if bit[i]:
                    print(A[i], end=' ',)
            print()

    else:
        candidate = [0, 1]
        for x in candidate:
            bit[i] = x
            f(i+1, N)
        # bit[i] = 1  # A[i]가 부분집합에 포함
        # f(i+1, N)
        # bit[i] = 0
        # f(i+1, N)


A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bit = [0] * 10
answer = 0
f(0, 10)
print(answer)
