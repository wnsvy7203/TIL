for _ in range(int(input())):
    string = input()
    num = int(string, 16)                           # num 은 받은 숫자를 변환 16진수
    output = ''                                     # 수업 때 쓴 함수 활용
    for i in range(len(string) * 4 - 1, -1, -1):    # 16진수이므로, string * 4 만큼 만들어야 한다.
        output += '1' if num & (1 << i) else '0'

    while output:                                   # output 이 남아있을 때까지 반복하도록
        new = output[0:7]                           # 7개씩 끊고
        output = output[7:]                         # output 을 7부터 다시 인덱싱

        result = int(new, 2)                        # 2진수를 10진수로 변환하세요

        print(result, end=' ')
    print()
