# silver 5
# 76ms

N = int(input())
heavy = []                              # 비교해야 하니까 x, y 값을 저장할 리스트도 만들자
for i in range(N):
    x, y = map(int, input().split())    # x, y도 받는다.
    heavy.append([x, y])

for i in range(N):
    rank = 1                            # 비교대상이 없으면 1등이니까
    for j in range(N):
        if(heavy[i][0]) < heavy[j][0] and heavy[i][1] < heavy[j][1]:
            rank += 1                   # 덩치의 인자값을 비교해서 다 작으면 1을 더한다.
    print(rank, end = " ")              # 결과값이 한 줄이니까 end 를 바꿔준다.
