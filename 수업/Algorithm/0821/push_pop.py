def push(item, size):
    global top
    top += 1
    if top == size:
        print('overflow') # 디버깅용, 없어도 상관없음
    else:
        stack[top] = item

def pop():
    global top
    if top == -1:
        print('underflow') # 디버깅용
        return 0
    else:
        top -= 1
        return stack[top+1]

size = 10
stack = [0] * size
top = -1

push(10, size)
top += 1 # push(20)
stack[top] = 20

if top > -1:
    top -= 1
    print(stack[top+1])
