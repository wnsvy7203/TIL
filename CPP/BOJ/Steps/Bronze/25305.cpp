// Bronze 2. Cutline

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int N, k;

    cin >> N >> k;

    vector<int> nums;

    for (int i = 0; i < N; i++)
    {
        int score;

        cin >> score;

        nums.push_back(score);
    }

    sort(nums.begin(), nums.end(), greater<>());

    cout << nums[k-1];
}