# bronze 3
# 68ms

while True:
    a, b, c = map(int, input().split())
    if a == 0 or b == 0 or c == 0:
        break
    else:
        if c != max(a, b, c):
            if a == max(a, b, c):
                a, c = c, a
            elif b == max(a, b, c):
                b, c = c, b

        if (a ** 2) + (b ** 2) == (c ** 2):
            print('right')
        else:
            print('wrong')
