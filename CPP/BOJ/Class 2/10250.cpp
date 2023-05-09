// Bronze 3. ACM Hotel

#include <iostream>

using namespace std;

int T;
int H, W, N;

int main()
{
    cin >> T;

    for (int t = 0; t < T; t++)
    {
        cin >> H >> W >> N;

        int hotel[105][105];

        for (int i = 1; i <= H; i++)
        {
            for (int j = 1; j <= W; j++)
            {
                hotel[i][j] = i * 100 + j;
            }
        }

        int cnt = 0;

        for (int i = 1; i <= W; i++)
        {
            for (int j = 1; j <= H; j++)
            {
                cnt += 1;

                if (cnt == N)
                {
                    cout << hotel[j][i] << "\n";
                }
            }
        }
    }
}