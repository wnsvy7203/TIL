for _ in range(int(input())):
    string = input()
    num = int(string, 16)                           # num 은 받은 숫자를 변환 16진수
    output = ''                                     # 수업 때 쓴 함수 활용
    for i in range(len(string) * 4 - 1, -1, -1):    # 16진수이므로, string * 4 만큼 만들어야 한다.
        output += '1' if num & (1 << i) else '0'
    arr = ['001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101', '011001', '101111']
    cnt = 0
    while cnt < len(string) * 4:
        for i in range(10):
            check = output[cnt:cnt+6]
            if check == arr[i]:
                print(i, end=' ')
                cnt += 6
                break
        else:
            cnt += 1
    print()
