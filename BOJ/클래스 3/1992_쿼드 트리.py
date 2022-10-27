# silver 1
# 72ms

import sys


def quad_tree(start, end, n):
    if n == 1:
        print(video[start][end], end='')
        return

    if video[start][end] == 0:
        for i in range(start, start+n):
            for j in range(end, end+n):
                if video[i][j] != 0:
                    print('(', end='')
                    quad_tree(start, end, n // 2)
                    quad_tree(start, end + n // 2, n // 2)
                    quad_tree(start + n // 2, end, n // 2)
                    quad_tree(start + n // 2, end + n // 2, n // 2)
                    print(')', end='')
                    return
        else:
            print(video[start][end], end='')
            return
    else:
        for i in range(start, start+n):
            for j in range(end, end+n):
                if video[i][j] != 1:
                    print('(', end='')
                    quad_tree(start, end, n // 2)
                    quad_tree(start, end + n // 2, n // 2)
                    quad_tree(start + n // 2, end, n // 2)
                    quad_tree(start + n // 2, end + n // 2, n // 2)
                    print(')', end='')
                    return
        else:
            print(video[start][end], end='')
            return


N = int(sys.stdin.readline())
video = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

quad_tree(0, 0, N)
