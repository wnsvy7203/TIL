// Silver 3. Memorizing English Vocabulary is Painful
// 896ms

#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>

using namespace std;
int N, M;
vector<string> voca;
map<string, int> mp;
string str;

bool compare(string a, string b)
{   
    if (a.length() == b.length() && mp[a] == mp[b]) return a < b;
    else if (mp[a] == mp[b]) return a.length() > b.length();
    else return mp[a] > mp[b];
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;

    for (int i = 0; i < N; i++)
    {
        cin >> str;

        if (str.length() < M) continue;

        if (mp.find(str) == mp.end())
        {
            mp[str] = 1;
            voca.push_back(str);
        }
        else
            mp[str]++;            
        
    }

    sort(voca.begin(), voca.end(), compare);

    for (int i = 0; i < voca.size(); i++)
        cout << voca[i] << '\n';
}