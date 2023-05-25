#include <iostream>

using namespace std;

int main()
{
    string str = "push 123";

    int idx = 0;

    for (int i = 0; i < str.length(); i++)
    {
        if (str[i] == ' ')
        {
            idx = i + 1;
        }
    }

    cout << stoi(str.substr(idx, 7));
}