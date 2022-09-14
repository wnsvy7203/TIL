def find_root(v):
    for a in range(1, v+1):
        if par[a] == 0:
            return a


def preorder(n):
    if n:
        print(n, end=' ')
        preorder(ch1[n])
        preorder(ch2[n])


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

preorder(root)
print()
