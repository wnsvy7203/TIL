// Silver 2. Minecraft
// 128ms

#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N, M, B;
    vector<vector<int>> land(500, vector<int>(500, 0));

    cin >> N >> M >> B;

    int min = 257;
    int max = 0;

    int val = pow(2, 31)-1;
    int res = 0;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> land[i][j];

            if (min > land[i][j]) min = land[i][j];
            if (max < land[i][j]) max = land[i][j];
        }
    }

    for (int h = min; h <= max; h++)
    {
        int up = 0;
        int down = 0;

        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
            {
                if (land[i][j] >= h) down += land[i][j] - h;
                else up += h - land[i][j];
            }
        }

        if (up > down + B) continue;

        int cnt = up + down * 2;

        if (cnt <= val)
        {
            val = cnt;
            res = h;
        }
    }
    
    cout << val << ' ' << res;
}