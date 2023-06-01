// Silver 4. I'm the Pockmon Master Lee Dasom
// 180ms

#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N, M;
    vector<string> pok(100001, "");
    map<string, int> check;

    cin >> N >> M;

    for (int i = 1; i <= N; i++)
    {
        string str;

        cin >> str;

        pok[i] = str;
        check.insert(make_pair(str, i));
    }
    
    while (M--)
    {
        string str;

        cin >> str;

        if (isdigit(str[0]))
            cout << pok[stoi(str)] << '\n';
        else
        {
            auto it = check.find(str);
            cout << it -> second << '\n';
        }
    }
}