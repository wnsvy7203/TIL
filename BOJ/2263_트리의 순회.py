import sys


def preorder(x):
    if x:
        print(x, end=' ')
        preorder(ch1[n])
        preorder(ch2[n])


n = int(sys.stdin.readline())
inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))

ch1 = [0 for _ in range(n+1)]
ch2 = [0 for _ in range(n+1)]

for i in range(2, n):
    pass
