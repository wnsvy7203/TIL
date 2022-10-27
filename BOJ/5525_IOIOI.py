import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()

P = ''
for i in range(2*N + 1):
    if i % 2:
        P += 'O'
    else:
        P += 'I'

S = S[S.find(P):]
cnt = 0
while True:
    if P in S:
        S = S[S.find(P)+2*N-2:]
        cnt += 1
    else:
        break

print(cnt)
