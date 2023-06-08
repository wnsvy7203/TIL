// Silver 3. Climbing Stairs

#include <iostream>
#include <vector>
#include <algorithm>

// 2번 연속으로는 밟을 수 있다.
// 현재 위치가 stairs[i]일 때 가능한 경우의 수를 구분해보면,
// 1. stairs[i-3], stairs[i-2]를 밟고 온 경우
// 2. stairs[i-3], stairs[i-1]를 밟고 온 경우

using namespace std;

int main()
{
    int N;
    vector<int> stairs(301, 0);
    vector<int> dp(301, 0);

    cin >> N;

    for (int i = 1; i <= N; i++)
    {
        int score;

        cin >> score;

        stairs[i] = score;
    }

    dp[1] = stairs[1];
    dp[2] = dp[1] + stairs[2];
    
    for (int i = 3; i < N+1; i++)
        dp[i] = max(dp[i-3] + stairs[i-1], dp[i-2]) + stairs[i];

    cout << dp[N];
}