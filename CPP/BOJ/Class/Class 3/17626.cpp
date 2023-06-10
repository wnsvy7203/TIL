// Silver 3. Four Squares
// 16ms

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main()
{
    int N;
    vector<int> dp(50001, 4);

    cin >> N;

    for (int i = 0; i < 4; i++)
        dp[i] = i;

    for (int i = 4; i < 50001; i++)
    {
        if (pow((int)sqrt(i), 2) == i)
            dp[i] = 1;
        else
        {
            int j = 1;
            while (j * j <= i)
            {
                dp[i] = min(dp[i], dp[i-j*j] + dp[j*j]);
                j++;
            }
        }
    }

    cout << dp[N];
}