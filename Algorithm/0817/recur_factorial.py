from tkinter import N


def f(n):
    if n == 0:
        return 1
    else:
        return n * f(n-1)

for i in range(21):
    print(i, f(i))