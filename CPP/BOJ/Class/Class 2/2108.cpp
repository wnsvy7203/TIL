// Silver 2. Statistics
// 200ms

#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>

using namespace std;

int main()
{
    int N;
    vector<int> nums(500001, 0);
    vector<int> most(8001, 0);

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        cin >> nums[i];

        most[nums[i]+4000]++;
    }
    
    sort(nums.begin(), nums.begin()+N);

    int res1 = (int)round((double)accumulate(nums.begin(), nums.begin()+N, 0) / N);

    int res2 = nums[N/2];

    int res3 = 0;

    int max = *max_element(most.begin(), most.end());
    vector<int> ans;

    for (int i = 0; i < most.size(); i++)
    {
        if (most[i] == max)
            ans.push_back(i-4000);
    }

    if (ans.size() >= 2) res3 = ans[1];
    else res3 = ans[0];

    int res4 = nums[N-1] - nums[0];

    cout << res1 << '\n' << res2 << '\n' << res3 << '\n' << res4;
}