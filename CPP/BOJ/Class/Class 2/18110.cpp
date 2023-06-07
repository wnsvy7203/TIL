// Silver 4. solved.ac
// 108ms

#include <iostream>
#include <queue>
#include <cmath>
#include <algorithm>
#include <numeric>

using namespace std;

int main()
{
    int n;

    cin >> n;

    if (!n)
    {
        cout << 0;
        return 0;
    }

    priority_queue<int> que;

    for (int i = 0; i < n; i++)
    {
        int opi;

        cin >> opi;

        que.push(opi);
    }

    int del = round(0.15 * n);

    for (int i = 0; i < del; i++)
        que.pop();

    int ans = 0;

    int w = que.size()-del;
    int cnt = 0;

    while (w--)
    {
        ans += que.top();
        cnt++;
        que.pop();
    }

    cout << round((double)ans / cnt) << '\n';
}