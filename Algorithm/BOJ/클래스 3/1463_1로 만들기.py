# silver 3
# 596ms

X = int(input())
cal = [0 for _ in range(X+1)]

for x in range(2, X+1):
    if not x % 3 and not x % 2:
        cal[x] = min(cal[x//3]+1, cal[x//2]+1, cal[x-1]+1)

    elif not x % 3 and x % 2:
        cal[x] = min(cal[x//3]+1, cal[x-1]+1)

    elif not x % 2 and x % 3:
        cal[x] = min(cal[x//2]+1, cal[x-1]+1)

    else:
        cal[x] = cal[x-1] + 1

print(cal[X])
