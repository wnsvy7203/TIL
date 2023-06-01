// Silver 4. Who Knows?
// 108ms

#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main()
{
    set<string> hear, watch;
    int N, M;

    cin >> N >> M;

    string str;

    for (int i = 1; i <= N; i++)
    {
        cin >> str;
        hear.insert(str);
    }

    int cnt = 0;

    for (int i = 1; i <= M; i++)
    {
        cin >> str;

        if (hear.find(str) != hear.end())
            watch.insert(str);
    }

    set<string>::iterator it;

    cout << watch.size() << '\n';

    for (it = watch.begin(); it != watch.end(); it++)
    {
        cout << *it << '\n';
    }
}