// Silver 3. 2*n Tiling 2

#include <iostream>
#include <vector>

using namespace std;

int n;
vector<int> dp(1001, 0);

void tile()
{
    dp[1] = 1;
    dp[2] = 3;

    for (int i = 3; i <= 1000; i++)
        dp[i] = (2 * dp[i-2] + dp[i-1]) % 10007;
}

int main()
{
    cin >> n;

    tile();

    cout << dp[n];
}