def baby_gin(s, k):
    if s == k:
        tri = 0
        run = 0

        if arr[0] == arr[1] == arr[2]:
            tri += 1
        if arr[3] == arr[4] == arr[5]:
            tri += 1
        if arr[0] + 1 == arr[1] and arr[1] + 1 == arr[2]:
            run += 1
        if arr[3] + 1 == arr[4] and arr[4] + 1 == arr[5]:
            run += 1

        if tri + run == 2:
            return True
        else:
            return False
    else:
        for i in range(s, k):
            arr[s], arr[i] = arr[i], arr[s]
            if baby_gin(s+1, k):
                return True
            arr[s], arr[i] = arr[i], arr[s]    # 되돌리기
        return False


for _ in range(int(input())):
    arr = list(map(int, input()))
    print(baby_gin(0, 6))
