// Silver 3. Padovan Sequence

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int T;

    cin >> T;

    vector<long long int> dp(101, 1);

    for (int i = 4; i <= 100; i++)
        dp[i] = dp[i-2] + dp[i-3];

    while (T--)
    {
        int N;

        cin >> N;

        cout << dp[N] << '\n';
    }
}