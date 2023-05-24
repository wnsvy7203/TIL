// Silver 5. Sorting Numbers 2
// 676ms

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int N;

    cin >> N;

    vector<int> nums;
    
    for (int i = 0; i < N; i++)
    {
        int num;

        cin >> num;

        nums.push_back(num);
    }

    sort(nums.begin(), nums.end());

    for (int i = 0; i < N; i++)
    {
        cout << nums[i] << '\n';
    }
}