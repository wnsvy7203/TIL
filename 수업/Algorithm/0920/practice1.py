for _ in range(int(input())):
    string = input()                                # 문자열로 받고
    while string:                                   # string 이 남아있을 때까지 반복하도록
        new = string[0:7]                           # 7개씩 끊고
        string = string[7:]                         # string 을 7부터 다시 인덱싱

        result = int(new, 2)

        print(result, end=' ')
    print()
