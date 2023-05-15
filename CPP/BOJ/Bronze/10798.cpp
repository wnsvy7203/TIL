// Bronze 1. Vertical Reading

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    vector<vector<char>> words;

    int max = 0;

    for (int i = 0; i < 5; i++)
    {
        vector<char> word;
        string str;

        cin >> str;

        if (max < str.length())
        {
            max = str.length();
        }

        for (int j = 0; j < str.length(); j++)
        {
            word.push_back(str[j]);
        }
        words.push_back(word);
    }

    for (int i = 0; i < 5; i++)
    {
        int size = words[i].size();

        if (size < max)
        {
            for (int j = 1; j <= max-size; j++)
            {
                words[i].push_back(' ');
            }
        }
    }

    for (int i = 0; i < max; i++)
    {
        for (int j = 0 ; j < 5; j++)
        {
            if (words[j][i] != ' ')
            {
                cout << words[j][i];
            }
        }
    }
}