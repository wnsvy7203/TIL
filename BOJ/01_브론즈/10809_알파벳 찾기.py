# bronze 5
# 76ms

S = input()

for s in 'abcdefghijklmnopqrstuvwxyz':
    if s in S:
        print(S.index(s), end=' ')
    else:
        print(-1, end=' ')
