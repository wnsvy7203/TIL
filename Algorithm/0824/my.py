p = 1
q = []

N = 20
m = 0

while m < N:
    q.append((p, 1, 0))

    v, c, my = q.pop(0)

    m += c
    q.append((v, c+1, my+c))
    p += 1

print(f'마지막 받은 사람: {v}')