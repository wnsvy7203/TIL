while True:
    try:
        A, B = map(int, input().split())
        if 0 < A < 10 and 0 < B < 10:
            print(A + B)
        else:
            break
    except:
        break
