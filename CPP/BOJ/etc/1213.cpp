// Silver 3. Making Pellindrom

#include <iostream>
#include <algorithm>

using namespace std;

string str;
int alphabet[26] = {0, };

int main()
{
    cin >> str;

    int N = str.length();

    for (int i = 0; i < N; i++)
        alphabet[str[i]-65]++;
    
    int cnt = 0;

    for (int i = 0; i < 26; i++)
        if (alphabet[i] % 2)
            cnt++;
        
    if (cnt > 1)
    {
        cout << "I'm Sorry Hansoo";
        return 0;
    }

    string res = "";

    for (int i = 0; i < N; i++)
        res += ' ';
    
    for (int i = 0; i < 26; i++)
    {
        if (alphabet[i] % 2)
        {
            res[N/2] = i+65;
            alphabet[i]--;
        }
        
        if (alphabet[i])
        {
            while (alphabet[i])
            {
                for (int j = 0; j < N/2; j++)
                    if (res[j] == ' ')
                    {
                        res[j] = i+65;
                        res[N-1-j] = i+65;
                        alphabet[i] -= 2;
                        break;
                    }
            }
        }
    }

    cout << res;
}