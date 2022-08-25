N = int(input())

if N == 1:
    print(1)
else:
    for i in range(N):
        if (3*(i**2)) + 3*i + 2 <= N < 3*((i+1)**2) + 3*(i+1) + 2:
            print(i+2)
            break

