// Silver 3. Different String's Count
// 512ms

#include <iostream>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    string S;
    cin >> S;

    int N = S.size();
    set<string> str;


    for (int i = 0; i < N; i++)
    {
        string s = "";
        for (int j = i; j < N; j++)
        {
            s += S[j];
            str.insert(s);
        }
    }

    cout << str.size();
}