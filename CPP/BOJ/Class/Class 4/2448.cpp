// Gold 4. Pointing Stars - 11
// 476ms

#include <iostream>
#include <cstring>

using namespace std;

int N;
char star[3072][6144];

void stars(int r, int c, int n)
{
    if (n == 3)
    {
        star[r][c] = '*';
        
        star[r+1][c-1] = '*';
        star[r+1][c+1] = '*';

        star[r+2][c-2] = '*';
        star[r+2][c-1] = '*';
        star[r+2][c] = '*';
        star[r+2][c+1] = '*';
        star[r+2][c+2] = '*';
    }
    else
    {
        stars(r, c, n/2);
        stars(r+n/2, c-n/2, n/2);
        stars(r+n/2, c+n/2, n/2);
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cout.tie(0);

    cin >> N;

    memset(star, ' ', sizeof(star));

    stars(0, N-1, N);

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < 2*N-1; j++)
            cout << star[i][j];
        cout << '\n';
    }
}