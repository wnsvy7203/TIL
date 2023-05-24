// Silver 5. Sort Inside

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    string N;

    cin >> N;

    vector<int> nums;

    for (int i = 0; i < N.length(); i++)
    {
        nums.push_back(N[i] - 48);
    }

    sort(nums.begin(), nums.end(), greater<>());

    for (int i = 0; i < N.length(); i++)
    {
        cout << nums[i];
    }
}