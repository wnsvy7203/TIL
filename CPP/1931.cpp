// Silver 1. Meeting Room Assignment
// 88ms

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;

int main()
{
    cin >> N;
    vector<pair<int, int>> time;

    for (int i = 0; i < N; i++)
    {
        int end, start;

        cin >> start >> end;

        time.push_back(make_pair(end, start));
    }

    sort(time.begin(), time.end());

    int end = time[0].first;
    int ans = 1;
    
    for (int i = 1; i <= N; i++)
    {
        if (time[i].second >= end)
        {
            ans++;
            end = time[i].first;
        }
    }

    cout << ans;
}