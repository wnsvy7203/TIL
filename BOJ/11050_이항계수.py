# 음이 아닌 정수 n, k에 대하여 이항계수(n, k)는
# (1+t) ** n을 전개하였을 때, t ** k의 계수
# 이항계수 (n, k)는 n! / (k! * (n - k)!)
import sys

N, K = map(int, sys.stdin.readline().split())

memo = [[1, 1], [1, 2, 1]]
for i in range(N):

