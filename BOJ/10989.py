import sys

N = int(sys.stdin.readline())            # 1 <= N <= 10000000
# 최대 천만 개의 수 정렬
# 주어지는 수는 10000보다 작거나 같은 자연수

num = [0] * 10001

for _ in range(N):
    num[int(sys.stdin.readline())] += 1

for i in range(10001):
    while num[i] > 0:
        print(i)
        num[i] -= 1
