// Gold 5. String Explosion
// 12ms

#include <iostream>
#include <string>

using namespace std;

string str;
string bomb;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> str >> bomb;

    string ans = "";

    for (int i = 0; i < str.size(); i++)
    {
        ans += str[i];

        if (str[i] == bomb[bomb.size()-1])
        {
            bool flag = 1;
            int idx = ans.size()-1;
            for (int j = bomb.size()-1; j >= 0; j--)
            {
                if (ans[idx] != bomb[j])
                {
                    flag = 0;
                    break;
                }
                idx--;
            }

            if (flag)
                ans.erase(ans.end()-bomb.size(), ans.end());
        }
    }

    if (ans.size())
        cout << ans;
    else
        cout << "FRULA";
}