#include <iostream>
#include <string>

using namespace std;

int main()
{
    int N;
    string nums;

    cin >> N;
    cin >> nums;

    int sum = 0;

    for (int i = 0; i < nums.length(); i++)
    {
        sum += nums[i] - 48;
    }

    cout << sum;
}