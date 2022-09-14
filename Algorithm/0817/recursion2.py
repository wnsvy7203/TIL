
def f(i, n):
    if i == n:
        return
    else:
        print(A[i])
        f(i+1, n)


N = 3
A = [1, 2, 3]
f(0, N)
