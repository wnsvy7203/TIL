N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

maxV = 0

for i in range(N):
    rs = 0 # 행의 합
    for j in range(N): # i행의 j열에 접근
        rs += arr[i][j]
    if maxV < rs:
        maxV = rs
print(maxV)