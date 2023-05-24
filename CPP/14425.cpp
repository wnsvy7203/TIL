// Silver 3. String Set

#include <iostream>
#include <set>
#include <string>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N, M;

    cin >> N >> M;

    set<string> S;

    for (int i = 0; i < N; i++)
    {
        string str;

        cin >> str;

        S.insert(str);
    }

    int cnt = 0;

    for (int i = 0; i < M; i++)
    {
        string str;

        cin >> str;
    }
    
    cout << cnt;
}