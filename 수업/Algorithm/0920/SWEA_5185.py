# 133ms

T = int(input())

for t in range(1, T+1):
    N, string = map(str, input().split())
    num = int(string, 16)
    output = ''
    for i in range(len(string) * 4 - 1, -1, -1):  # 16진수이므로, string * 4 만큼 만들어야 한다.
        output += '1' if num & (1 << i) else '0'

    print(f'#{t} {output}')
