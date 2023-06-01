// Silver 5. Set

#include <iostream>
#include <set>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int M;
    set<int> S;

    cin >> M;

    while (M--)
    {
        string str;

        cin >> str;

        if (str == "add")
        {
            int x;
            cin >> x;

            S.insert(x);
        }
        else if (str == "remove")
        {
            int x;
            cin >> x;

            S.erase(x);
        }
        else if (str == "check")
        {
            int x;
            cin >> x;

            if (S.count(x)) cout << 1 << '\n';
            else cout << 0 << '\n';
        }
        else if (str == "toggle")
        {
            int x;
            cin >> x;

            if (S.count(x)) S.erase(x);
            else S.insert(x);
        }
        else if (str == "all")
        {
            for (int i = 1; i <= 20; i++)
                S.insert(i);
        }
        else if (str == "empty")
            S.clear();
    }
}