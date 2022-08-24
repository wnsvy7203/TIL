N = 3
q = [0] * N
front = -1
rear = -1

rear += 1
q[rear] = 1

rear += 1
q[rear] = 2

rear += 1
q[rear] = 3

front += 1
print(q[front])

front += 1
print(q[front])

front += 1
print(q[front])