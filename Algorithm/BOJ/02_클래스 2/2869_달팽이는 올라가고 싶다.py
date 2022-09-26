# silver 5
# 72ms

A, B, V = map(int, input().split())


def roundup(n):
    if n == int(n):
        return n
    else:
        return int(n) + 1


print(int(roundup((V-A)/(A-B))+1))
