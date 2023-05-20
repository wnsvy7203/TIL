// Silver 5. Croatian Alphabet

#include <iostream>
#include <string>

using namespace std;

int main()
{
    string str;

    cin >> str;

    int cnt = 0;

    for (int i = 0; i < str.length(); i++)
    {
        if (str[i] == '=')
        {
            continue;
        }
        else if (str[i] == '-')
        {
            continue;
        }
        else if (str[i] == 'z' && i != str.length()-1)
        {
            if (str[i-1] == 'd' && str[i+1] == '=')
            {
                continue;
            }
            else
            {
                cnt++;
            }
        }
        else if (str[i] == 'j')
        {
            if (str[i-1] == 'l' || str[i-1] == 'n')
            {
                continue;
            }
            else
            {
                cnt++;
            }
        }
        else
        {
            cnt++;
        }
    }

    cout << cnt;
}