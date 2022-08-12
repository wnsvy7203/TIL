num = 456789
cnt = [0] * 12

for i in range(6):
    cnt[num % 10] += 1
    num //= 10
i = 0
tri = run = 0
while i < 10:
    if cnt[i] >= 3:
        cnt[i] -= 3
        tri += 1
        continue
    if cnt[i] >= 1 and cnt[i+1] >= 1 and cnt[i+2] >= 1:
        cnt[i] -= 1
        cnt[i+1] -= 1
        cnt[i+2] -= 1
        run += 1
        continue
    i += 1
if run + tri == 2:
    print('Baby Gin')
else:
    print('Lose')