// Silver 4. Deque

#include <iostream>
#include <deque>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N;

    cin >> N;

    deque<int> que;

    while (N--)
    {
        string str;

        cin >> str;

        if (str == "push_front")
        {
            int X;

            cin >> X;

            que.push_front(X);
        }
        else if (str == "push_back")
        {
            int X;

            cin >> X;
            
            que.push_back(X);
        }
        else if (str == "pop_front")
        {
            if (!que.empty())
            {
                cout << que.front() << '\n';
                que.pop_front();
            }
            else cout << -1 << '\n';
        }
        else if (str == "pop_back")
        {
            if (!que.empty())
            {
                cout << que.back() << '\n';
                que.pop_back();
            }
            else cout << -1 << '\n';
        }
        else if (str == "size")
            cout << que.size() << '\n';
        else if (str == "empty")
            cout << que.empty() << '\n';
        else if (str == "front")
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
    }
}