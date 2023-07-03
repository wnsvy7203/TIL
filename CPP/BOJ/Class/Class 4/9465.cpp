// Silver 1. Sticker
// 92ms

#include <iostream>
#define MAX 100001

using namespace std;

int T;
int stickers[MAX][2];
int dp[MAX][2];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> T;

    int n;

    while (T--)
    {
        cin >> n;

        for (int i = 0; i < n; i++)
            cin >> stickers[i][0];
        for (int i = 0; i < n; i++)
            cin >> stickers[i][1];

        dp[0][0] = stickers[0][0];
        dp[0][1] = stickers[0][1];

        dp[1][0] = dp[0][1] + stickers[1][0];
        dp[1][1] = dp[0][0] + stickers[1][1];

        for (int i = 2; i < n; i++)
        {
            dp[i][0] = max(dp[i-2][1], dp[i-1][1]) + stickers[i][0];
            dp[i][1] = max(dp[i-2][0], dp[i-1][0]) + stickers[i][1];
        }

        cout << max(dp[n-1][0], dp[n-1][1]) << '\n';
    }
}