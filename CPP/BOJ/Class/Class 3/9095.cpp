// Silver 3. Add 1, 2, 3

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int T;
    vector<int> dp(12, 0);

    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;

    for (int i = 4; i <= 11; i++)
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1];

    cin >> T;

    while (T--)
    {
        int n;

        cin >> n;

        cout << dp[n] << '\n';
    }
}