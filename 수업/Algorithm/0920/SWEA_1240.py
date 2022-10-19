# 단순 이진 암호코드

for C in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    flag = True
    result = 0
    cnt = 0

    string_list = [input() for _ in range(N)]

    for i in range(N):
        if '1' not in string_list[i]:
            continue
        else:
            new = string_list[i][::-1]

    for i in range(M):
        if new[i] == '0':
            continue
        elif new[i] == '1':
            new = new[i:i+56]
            new = new[::-1]
            break

    for i in range(8):
        output = new[7*i:7*i+7]
        if output not in arr:
            flag = False
            break
        else:
            for k in range(10):
                if output == arr[k]:
                    cnt += k
                    if not i % 2:
                        result += k*3
                        break
                    else:
                        result += k
                        break

    if flag:
        if not result % 10:
            print(f'#{C} {cnt}')
        else:
            print(f'#{C} {0}')
    else:
        print(f'#{C} {0}')
