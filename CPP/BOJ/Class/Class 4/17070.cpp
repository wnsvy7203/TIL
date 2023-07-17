// Gold 5. Moving Pipe 1

#include <iostream>
#include <queue>

using namespace std;

int N;
int home[17][17];
int dp[17][17][3];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;

    for (int i = 1; i <= N; i++)
        for (int j = 1; j <= N; j++)
            cin >> home[i][j];
    
    dp[1][2][0] = 1;
    
    for (int i = 3; i <= N; i++)
        if (!home[1][i])
            dp[1][i][0] = dp[1][i-1][0];
    
    for (int i = 2; i <= N; i++)
        for (int j = 3; j <= N; j++)
            if (!home[i][j])
            {
                dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1];
                dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2];
                if (!home[i-1][j] && !home[i][j-1])
                    dp[i][j][1] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2];
            }

    cout << dp[N][N][0] + dp[N][N][1] + dp[N][N][2];
}