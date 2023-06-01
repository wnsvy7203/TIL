// Silver 4. Coin 0

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int N, K;
    vector<int> coin(11, 0);

    cin >> N >> K;

    for (int i = 1; i <= N; i++)
        cin >> coin[i];

    int cnt = 0;
    
    for (int i = N; i > 0; i--)
    {
        if (coin[i] > K) continue;
        else
        {
            int div = K / coin[i];

            cnt += div;
            K -= div * coin[i];
        }
    }

    cout << cnt;
}