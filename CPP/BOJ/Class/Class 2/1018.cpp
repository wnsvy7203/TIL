// Silver 4. re-Coloring the Chess Board

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int N, M;
char board[50][50] = {' ', };

int pattern_w(int a, int b)
{
    int cnt = 0;

    for (int y = 0; y < 8; y++)
        if (!(y % 2))
        {
            for (int x = 0; x < 8; x += 2)
                if (board[a+y][b+x] != 'W')
                    cnt++;
            for (int x = 1; x < 8; x += 2)
                if (board[a+y][b+x] == 'W')
                    cnt++;
        }
        else
        {
            for (int x = 0; x < 8; x += 2)
                if (board[a+y][b+x] == 'W')
                    cnt++;
            for (int x = 1; x < 8; x += 2)
                if (board[a+y][b+x] != 'W')
                    cnt++;
        }
    
    return cnt;
}

int pattern_b(int a, int b)
{
    int cnt = 0;

    for (int y = 0; y < 8; y++)
        if (!(y % 2))
        {
            for (int x = 0; x < 8; x += 2)
                if (board[a+y][b+x] != 'B')
                    cnt++;
            for (int x = 1; x < 8; x += 2)
                if (board[a+y][b+x] == 'B')
                    cnt++;
        }
        else
        {
            for (int x = 0; x < 8; x += 2)
                if (board[a+y][b+x] == 'B')
                    cnt++;
            for (int x = 1; x < 8; x += 2)
                if (board[a+y][b+x] != 'B')
                    cnt++;
        }
    
    return cnt;
}

int min(int a, int b)
{
    if (pattern_w(a, b) > pattern_b(a, b)) return pattern_b(a, b);
    else return pattern_w(a, b);
}

int main()
{
    cin >> N >> M;

    for (int i = 0; i < N; i++)
    {
        string str;

        cin >> str;

        for (int j = 0; j < M; j++)
            board[i][j] = str[j];
    }

    int minV = 65;

    for (int i = 0; i <= N-8; i++)
        for (int j = 0; j <= M-8; j++)
            if (min(i, j) < minV)
                minV = min(i, j);
    
    cout << minV;
}