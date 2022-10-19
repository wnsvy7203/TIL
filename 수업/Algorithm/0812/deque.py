from collections import deque

A = deque(range(1, 15))

B = list(A)
B.sort(reverse=True)
A = deque(B)
print(A)