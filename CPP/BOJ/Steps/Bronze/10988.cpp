// Bronze 2. Check whether Pellindrom or not

#include <iostream>
#include <string>

using namespace std;

int main()
{
    string str;

    cin >> str;

    bool check = true;

    for (int i = 0; i < str.length() / 2; i++)
    {
        if (str[i] != str[str.length()-1-i])
        {
            check = false;
        }
    }

    cout << (int)check;
}