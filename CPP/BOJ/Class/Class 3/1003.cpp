// Silver 3. Fibonacci Function

#include <iostream>
#include <vector>

using namespace std;

int T;
vector<int> cnt0 = {1, 0};
vector<int> cnt1 = {0, 1};

void fibo()
{
    for (int i = 2; i <= 40; i++)
    {
        cnt0.push_back(cnt0[i-2] + cnt0[i-1]);
        cnt1.push_back(cnt1[i-2] + cnt1[i-1]);
    }
}

int main()
{
    int T;

    cin >> T;

    fibo();

    while (T--)
    {
        int N;

        cin >> N;

        cout << cnt0[N] << ' ' << cnt1[N] << '\n';
    }
}