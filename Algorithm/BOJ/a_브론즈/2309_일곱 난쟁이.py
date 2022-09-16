# Bronze 1
# 68ms

# 9개의 원소를 갖는 리스트, 딕트, 세트
# 세트는 중복되면 삭제하니까 안 되겠다.

# 방법 1
# 중에 원소가 7개인 부분집합의 개수
# 는 36개네
# 이 부분집합 중 합이 100인 경우 print
# 나중에 해 볼 것

# 방법 2
# 2개 빼고, 남은 원소의 합이 100이면 print

H = [int(input()) for _ in range(9)]
sum_H = sum(H)
for i in range(8):
    for j in range(i+1, 9):
        if sum_H - H[i] - H[j] == 100:
            a = H[i]
            b = H[j]
            break

H.remove(a)
H.remove(b)
H.sort()
for i in H:
    print(i, end='\n')
