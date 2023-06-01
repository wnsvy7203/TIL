#include <iostream>
#include <vector>
#include <numeric>
#include <cmath>

using namespace std;

int main()
{
    vector<int> nums = { -1, -2, -3, -1, -2 };

    cout << accumulate(nums.begin(), nums.begin()+5, 0);
}