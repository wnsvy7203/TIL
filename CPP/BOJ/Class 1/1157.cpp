// Bronze 1. Studying Words
// 44ms

#include <iostream>
#include <string>

using namespace std;

int main()
{
    string word;

    cin >> word;

    for (int i = 0; i < word.length(); i++)
    {
        if (word[i] >= 97 && word[i] <= 122)
        {
            word[i] -= 32;
        }
    }

    int alphabet[26] = { 0 };
    bool many = false;

    for (int i = 0; i < word.length(); i++)
    {
        alphabet[word[i] - 65]++;
    }

    int res = 0;
    int idx = 0;

    for (int i = 0; i < 26; i++)
    {
        if (alphabet[i] > res)
        {
            res = alphabet[i];
            idx = i;
        }
    }

    for (int i = 0; i < 26; i++)
    {
        if (alphabet[i] == res && idx != i)
        {
            many = true;
        }
    }

    if (many == true)
    {
        cout << "?";
    }
    else
    {
        cout << char(idx + 65);
    }
}