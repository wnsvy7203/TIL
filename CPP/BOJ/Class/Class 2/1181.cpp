// Silver 5. Sorting Words
// 92ms

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(string a, string b)
{
    if (a.length() != b.length())
    {
        return a.length() < b.length();
    }
    else
    {
        return a < b;
    }
}

int main()
{
    int N;

    cin >> N;

    vector<string> str;

    for (int i = 0; i < N; i++)
    {
        string word;

        cin >> word;

        str.push_back(word);
    }

    sort(str.begin(), str.end(), compare);

    for (int i = 0; i < str.size(); i++)
    {
        if (i != 0 && str[i] == str[i-1])
        {
            continue;
        }

        cout << str[i] << '\n';
    }
}