# bronze 4
# 72ms

N = int(input())
for i in range(N):
    for _ in range(N-i-1):
        print(' ', end='')
    for _ in range(i+1):
        print('*', end='')
    print()
