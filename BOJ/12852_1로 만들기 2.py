import sys

N = int(sys.stdin.readline())
res = [N]
cnt = 0
while N != 1:
    if not N % 3:
        cnt += 1
        N //= 3
        res.append(N)
    elif not N % 2:
        cnt += 1
        N //= 2
        res.append(N)
    else:
        cnt += 1
        N -= 1
        res.append(N)

print(cnt)
print(*res)