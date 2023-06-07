// Silver 4. Finding Password
// 212ms

#include <iostream>
#include <map>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N, M;
    map<string, string> info;

    cin >> N >> M;

    for (int i = 0; i < N; i++)
    {
        string site;
        string pwd;

        cin >> site >> pwd;

        info.insert(make_pair(site, pwd));
    }

    while (M--)
    {
        string site;

        cin >> site;

        cout << info[site] << '\n';
    }
}