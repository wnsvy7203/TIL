// Gold 5. Ordinary Bag

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, K;
int dp[101][100001];
int weight[101];
int value[101];

int main()
{
    cin >> N >> K;

    for (int i = 1; i <= N; i++)
        cin >> weight[i] >> value[i];

    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= K; j++)
        {
            if (j >= weight[i])
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i]);
            else
                dp[i][j] = dp[i-1][j];
        }
    }

    cout << dp[N][K];
}