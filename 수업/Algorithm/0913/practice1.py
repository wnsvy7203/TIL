# 13
# 1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13


def find_root(v):
    for a in range(1, v+1):
        if par[a] == 0:
            return a


def preorder(n):
    if n:
        print(n, end=' ')
        preorder(ch1[n])
        preorder(ch2[n])


def inorder(n):
    if n:
        inorder(ch1[n])
        print(n, end=' ')
        inorder(ch2[n])


def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n, end=' ')


def f(n):
    if n == 0:
        return 0
    else:
        L = f(ch1[n])
        R = f(ch2[n])
        return L + R + 1


V = int(input())
arr = list(map(int, input().split()))
E = V-1

ch1 = [0] * (V+1)
ch2 = [0] * (V+1)
par = [0] * (V+1)
for i in range(0, 2*E, 2):
    p, c = arr[i], arr[i+1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c
    par[c] = p
root = find_root(V)

# preorder(root)
# print()
# inorder(root)
# print()
# postorder(root)
# print()

print(f(3))
