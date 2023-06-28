// Silver 3. Snail
// 100ms

#include <iostream>

using namespace std;

int N;
int num;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> num;

    int board[N][N] = {0, };
    int ans1;
    int ans2;

    int n = N;
    int start = N * N;
    int line = 0;

    while (start > 0)
    {
        for (int i = line; i < line+n; i++)
        {
            board[i][line] = start;
            if (start == num)
            {
                ans1 = i;
                ans2 = line;
            }
            start--;
        }

        for (int i = line+1; i < line+n; i++)
        {
            board[N-1-line][i] = start;
            if (start == num)
            {
                ans1 = N-1-line;
                ans2 = i;
            }
            start--;
        }

        for (int i = N-2-line; i >= line; i--)
        {
            board[i][N-1-line] = start;
            if (start == num)
            {
                ans1 = i;
                ans2 = N-1-line;
            }
            start--;
        }

        for (int i = N-2-line; i >= line+1; i--)
        {
            board[line][i] = start;
            if (start == num)
            {
                ans1 = line;
                ans2 = i;
            }
            start--;
        }

        n -= 2;
        line++;
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cout << board[i][j] << ' ';
        }
        cout << '\n';
    }

    cout << ans1+1 << ' ' << ans2+1;
}