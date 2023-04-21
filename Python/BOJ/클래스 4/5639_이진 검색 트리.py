# gold 4
# 3812ms

import sys
sys.setrecursionlimit(10 ** 6)


def postorder(s, e):
    if s > e:
        return

    mid = e + 1

    for i in range(s+1, e+1):
        if preorder[s] < preorder[i]:
            mid = i
            break

    postorder(s+1, mid-1)
    postorder(mid, e)
    print(preorder[s])


preorder = []
while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except ValueError:
        break

postorder(0, len(preorder) - 1)
