import sys

M, N = map(int, sys.stdin.readline().split())
<<<<<<< HEAD
lst = list(range(M, N+1))

for i in lst:
=======

for i in range(M, N+1):
>>>>>>> ba001036f750c93f2b6d483e4bb272d0f75450a9
    for j in range(2, i):
        if not i % j:
            break
    else:
        print(i)
