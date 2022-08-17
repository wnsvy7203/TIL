stackSize = 10
stack = [0] * stackSize
top = -1

top += 1            # push(1)
stack[top] = 1

top += 1            # push(2)
stack[top] = 2

top += 1            # push(3)
stack[top] = 3

top -= 1            # 뭘 먼저 하냐에 따라 다르다.
temp = stack[top+1] # top을 먼저 빼면 top + 1
print(temp)

temp = stack[top]   # 출력을 먼저 하면 top
top -= 1
print(temp)

temp = stack[top]
top -= 1
print(temp)
