// Silver 4. Zero

#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int K;

    cin >> K;

    vector<int> stk;

    for (int i = 0; i < K; i++)
    {
        int num;

        cin >> num;

        if (num)
            stk.push_back(num);
        else
            stk.pop_back();
    }

    int sum = accumulate(stk.begin(), stk.end(), 0);

    cout << sum;
}