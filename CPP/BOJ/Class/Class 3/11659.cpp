// Silver 3. Prefix Sum
// 40ms

#include <iostream>
#include <vector>

using namespace std;

int N, M;
vector<int> nums(100005, 0);
vector<int> sum(100005, 0);

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;

    for (int i = 1; i <= N; i++)
        cin >> nums[i];
    
    sum[1] = nums[1];

    for (int i = 2; i <= N; i++)
        sum[i] = sum[i-1] + nums[i];
    
    while (M--)
    {
        int i, j;

        cin >> i >> j;

        cout << sum[j] - sum[i-1] << '\n';
    }
}