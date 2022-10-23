# silver 1
# 68ms

import sys


def preorder(n):
    if n:
        print(chr(n+64), end='')
        preorder(ch1[n])
        preorder(ch2[n])


def inorder(n):
    if n:
        inorder(ch1[n])
        print(chr(n+64), end='')
        inorder(ch2[n])


def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(chr(n+64), end='')


N = int(sys.stdin.readline())

ch1 = [0 for _ in range(27)]
ch2 = [0 for _ in range(27)]

for _ in range(N):
    u, v, w = sys.stdin.readline().rstrip().split()

    if v != '.':
        ch1[ord(u)-64] = ord(v)-64

    if w != '.':
        ch2[ord(u)-64] = ord(w)-64

preorder(1)
print()
inorder(1)
print()
postorder(1)
