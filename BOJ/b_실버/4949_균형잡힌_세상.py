while True:
    string = input()
    stack = []

    if string == '.':
        break

    for i in string:
        if i == '(' or i == '[':
            stack.append(i)

        elif i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)

        elif i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(i)

    if stack:
        print('no')
    else:
        print('yes')
