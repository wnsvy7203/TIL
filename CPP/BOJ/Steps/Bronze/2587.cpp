// Bronze 2. Representative Value

#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int main()
{
    vector<int> nums(5);

    for (int i = 0; i < 5; i++)
    {
        int num;

        cin >> num;

        nums[i] = num;
    }

    sort(nums.begin(), nums.end());

    cout << accumulate(nums.begin(), nums.end(), 0) / 5 << '\n' << nums[2];
}