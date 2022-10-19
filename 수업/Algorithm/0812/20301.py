import sys
from collections import deque
input = sys.stdin.readline

N, K, M = map(int, input().split()) # (1 <= N <= 5000, 1 <= K, M <= N)
A = deque(range(1, N+1)) # 1부터 N까지의 디큐 선언

kill = 0
cnt = 1

while A: # A에 원소가 있을 때,
    if cnt % K: # cnt 가 K의 배수가 아니면
        a = A.popleft()
        A.append(a)
        cnt += 1
    else: # 
        b = A.popleft()
        print(b)
        cnt = 1
        kill += 1
    
    if kill == M:
        B = reversed(list(A))
        A = deque(B)
        cnt = 1
        kill = 0