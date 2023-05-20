// Bronze 1. Pellindrom

#include <iostream>
#include <string>

using namespace std;

int main()
{
    while (1)
    {
        string str;

        cin >> str;

        if (str == "0")
        {
            break;
        }

        bool check = 1;

        int L = str.length();

        for (int i = 0; i < L / 2; i++)
        {
            if (str[i] != str[L - 1 - i])
            {
                check = 0;
            }
        }

        if (check == 1)
        {
            cout << "yes" << '\n';
        }
        else
        {
            cout << "no" << '\n';
        }
    }
}