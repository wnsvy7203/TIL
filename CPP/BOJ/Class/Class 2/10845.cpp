// Silver 4. Queue

#include <iostream>
#include <string>
#include <queue>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N;

    cin >> N;

    queue<int> que;

    cin.ignore();

    while (N--)
    {
        string str;

        getline(cin, str);

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
        else if (str == "size") cout << que.size() << '\n';
        else if (str == "empty") cout << que.empty() << '\n';
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
        else que.push(stoi(str.substr(5, 7)));
    }
}