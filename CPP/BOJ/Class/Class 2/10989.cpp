// Bronze 1. Sort Numbers

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N;

    cin >> N;

    vector<int> nums(10005);

    for (int i = 0; i < N; i++)
    {
        int num;

        cin >> num;

        nums[num] += 1;
    }

    for (int i = 1; i < 10001; i++)
    {
        if (nums[i] != 0)
        {
            while (nums[i] > 0)
            {
                cout << i << '\n';

                nums[i] -= 1;
            }
        }
    }
}