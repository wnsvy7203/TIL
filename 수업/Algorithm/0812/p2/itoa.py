def itoa(tc):
    temp = ''
    minus = False

    if tc == 0:
        return chr(48)

    if tc < 0:
        minus = True
        tc = tc * (-1)

    while tc > 0:
        temp = chr((tc % 10) + 48) + temp
        tc //= 10

    if minus:
        temp = '-' + temp
    return temp

a = int(input())

print(itoa(a))