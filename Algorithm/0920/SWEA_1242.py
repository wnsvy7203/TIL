code_len = {
    (3, 2, 1, 1): 0,
    (2, 2, 2, 1): 1,
    (2, 1, 2, 2): 2,
    (1, 4, 1, 1): 3,
    (1, 1, 3, 2): 4,
    (1, 2, 3, 1): 5,
    (1, 1, 1, 4): 6,
    (1, 3, 1, 2): 7,
    (1, 2, 1, 3): 8,
    (3, 1, 1, 2): 9,
}

# hex_to_bin = {
#     '0': '0000',
#     '1': '0001',
#     '2': '0010',
#     '3': '0011',
#     '4': '0100',
#     '5': '0101',
#     '6': '0110',
#     '7': '0111',
#     '8': '1000',
#     '9': '1001',
#     'A': '1010',
#     'B': '1011',
#     'C': '1100',
#     'D': '1101',
#     'E': '1110',
#     'F': '1111',
# }

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
for C in range(1, T+1):
    N, m = map(int, input().split())
    M = m * 4
    string_list = list(set([input() for _ in range(N)]))
    pwd = []
    flag = True
    res = 0
    cnt = 0

    for i in range(len(string_list)):
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

    for i in range(len(pwd)):
        num = int(pwd[i], 16)
        new = ''
        for j in range(len(pwd[i]*4)-1, -1, -1):
            new += '1' if num & (1 << j) else '0'
        new = new[::-1]
        kk = len(new) // 56

        for j in range(len(new)):
            if new[j] == 0:
                continue
            else:
                new = new[j:56*kk]
                new = new[::-1]
                break

        for j in range(8*kk):
            put = new[7*j:7*j+7]
            if put not in pattern.values():
                flag = False
                break
            else:
                for k in range(10):
                    if put == pattern[k]:
                        cnt += k
                        if not i % 2:
                            res += k * 3
                            break
                        else:
                            res += k
                            break

        if not flag:
            cnt = 0
            flag = True

    if flag:
        pass

    # for i in range(len(new)):
    #     if new[i] == '0':
    #         continue
    #     elif new[i] == '1':
    #         new = new[i:i + 56]
    #         new = new[::-1]
    #         break
    #
    # for i in range(8):
    #     output = new[7 * i:7 * i + 7]
    #     if output not in arr:
    #         flag = False
    #         break
    #     else:
    #         for k in range(10):
    #             if output == arr[k]:
    #                 cnt += k
    #                 if not i % 2:
    #                     result += k * 3
    #                     break
    #                 else:
    #                     result += k
    #                     break
    #

