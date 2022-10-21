# silver 3
# 68ms

A, B = map(int, input().split())
cnt_left = 0
cnt_right = 0

a, b = A, B

# a > b이면 왼쪽으로 이동한 경우
# a < b이면 오른쪽으로 이동한 경우이다.

while a > 1 and b > 1:
    if a > b:
        cnt_left += a // b
        a %= b
    else:
        cnt_right += b // a
        b %= a

cnt_left += a - 1
cnt_right += b - 1

print(cnt_left, cnt_right)
