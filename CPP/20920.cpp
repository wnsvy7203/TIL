// Silver 3. Memorizing English Vocabulary is Painful

#include <iostream>
#include <set>
#include <string>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N, M;

    cin >> N >> M;

    set<string> voca;

    for (int i = 0; i < N; i++)
    {
        string str;

        cin >> str;

        if (str.size() >= M)
        {
            voca.insert(str);
        }
    }

    set<string>::iterator iter;

    for (iter = voca.begin(); iter != voca.end(); iter++)
    {
        cout << *iter << '\n';
    }
}