import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    infix = list(map(str, input().split()))
    postfix = []

    for i in infix:
        if i.isdigit():
            postfix.append(i)
        elif i == '+':
            if len(postfix) >= 2:
                a = postfix.pop()
                b = postfix.pop()
                postfix.append(int(a) + int(b))
            else:
                print(f'#{tc} error')
                break
        elif i == '-':
            if len(postfix) >= 2:
                a = postfix.pop()
                b = postfix.pop()
                postfix.append(int(b) - int(a))
            else:
                print(f'#{tc} error')
                break
        elif i == '*':
            if len(postfix) >= 2:
                a = postfix.pop()
                b = postfix.pop()
                postfix.append(int(a) * int(b))
            else:
                print(f'#{tc} error')
                break
        elif i == '/':
            if len(postfix) >= 2:
                a = postfix.pop()
                b = postfix.pop()
                postfix.append(int(b) // int(a))
            else:
                print(f'#{tc} error')
                break
        elif i == '.':
            print(f'#{tc}', *postfix)
