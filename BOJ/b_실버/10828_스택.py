import sys

N = int(sys.stdin.readline())
arr = [list(sys.stdin.readline().split()) for _ in range(N)]
stack = []

for i in arr:
    if i[0] == 'push':
        stack.append(i[1])

    if i == ['pop']:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif i == ['size']:
        print(len(stack))
    elif i == ['empty']:
        if stack:
            print(0)
        else:
            print(1)
    elif i == ['top']:
        if stack:
            print(stack[-1])
        else:
            print(-1)
