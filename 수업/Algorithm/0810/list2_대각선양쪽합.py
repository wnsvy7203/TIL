N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

s1 = 0
s2 = 0

for i in range(N):
    for j in range(N):
        if i > j:
            s1 += arr[i][j]
        else:
            s2 += arr[i][j]
if s1 > s2:
    print(s1)
else:
    print(s2)

s1 = 0
s2 = 0
for i in range(N):
    for j in range(i+1, N):
        s2 += arr[i][j]
        s1 += arr[j][i]

if s1 > s2:
    print(s1)
else:
    print(s2)