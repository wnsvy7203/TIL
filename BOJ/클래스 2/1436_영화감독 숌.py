# silver 5
# 844ms

import sys

N = int(sys.stdin.readline())

cnt = 0
num = 666
string = '666'
while True:
    if string in str(num):
        cnt += 1
    if cnt == N:
        print(num)
        break
    num += 1
