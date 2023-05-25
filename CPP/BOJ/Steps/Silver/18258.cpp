// Silver 4. Queue 2
// 376ms

#include <iostream>
#include <queue>
#include <string>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N;

    cin >> N;

    queue<int> que;

    N++;

    while (N--)
    {
        string str;

        getline(cin, str);

        if (str == "")
            continue;

        if (str == "front")
        {
            if (!que.empty())
                cout << que.front() << '\n';
            else
                cout << -1 << '\n';
        }
        else if (str == "back")
        {
            if (!que.empty())
                cout << que.back() << '\n';
            else
                cout << -1 << '\n';
        }
        else if (str == "size")
            cout << que.size() << '\n';
        else if (str == "empty")
            cout << que.empty() << '\n';
        else if (str == "pop")
        {
            if (!que.empty())
            {
                cout << que.front() << '\n';
                que.pop();
            }
            else
                cout << -1 << '\n';
        }
        else
            que.push(stoi(str.substr(5, 7)));
    }
}