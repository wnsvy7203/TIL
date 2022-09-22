pattern = {
    0: '0001101',
    1: '0011001',
    2: '0010011',
    3: '0111101',
    4: '0100011',
    5: '0110001',
    6: '0101111',
    7: '0111011',
    8: '0110111',
    9: '0001011',
}

T = int(input())
for C in range(1, T + 1):
    N, M = map(int, input().split())
    string_list = list(set([input().strip('0') for _ in range(N)]))
    pwd = []

    for i in range(len(string_list)):
<<<<<<< HEAD
        while string_list[i]:
            if '00000' in string_list[i]:
                idx = string_list[i].index('00000')
                pwd.append(string_list[i][:idx])
                string_list[i] = string_list[i][idx:]
                string_list[i] = string_list[i].lstrip('0')
            else:
                pwd.append(string_list[i])
                break

        if int(string_list[i], 16) == 0:
            continue
        else:
            output = ''
            for j in range(m):
                if string_list[i][j] == '0':
                    continue
                else:
                    output += string_list[i][j]
                    if string_list[i][j+1] == '0':
                        if output not in pwd:
                            pwd.append(output)
                        break
>>>>>>> cfe76269f107d006764903614ed031bba36e53fe

    pwd = list(set(pwd))

    cnt_list = []
    res = 0
    cnt = 0
    for i in range(len(pwd)):
        num = int(pwd[i], 16)
        output = ''
        for j in range(len(pwd[i] * 4) - 1, -1, -1):
            output += '1' if num & (1 << j) else '0'

        for j in range(len(output) - 1, -1, -1):
            if output[j] == '1':
                output = '0' * (len(output) - (j + 1)) + output[:j + 1]
                break

        mod = len(output) % 56
        div = len(output) // 56
        if mod:
            if mod > 28:
                output = '0' * (56 - mod) + output
                div += 1
            elif mod < 28:
                output = output[mod * div::]

        for j in range(0, 8 * div, div):
            put = output[7 * j:7 * j + 7 * div:div]

            for k in range(10):
                if put == pattern[k]:
                    cnt += k
                    if not (j // div) % 2:
                        res += k * 3
                        break
                    else:
                        res += k
                        break

        if res % 10:
            res = 0
            cnt = 0
        else:
            res = 0
            cnt_list.append(cnt)
            cnt = 0

    if not cnt_list:
        print(f'#{C} 0')
    else:
        print(f'#{C} {sum(cnt_list)}')
