// Bronze 2. OX Quiz
// 4ms

#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T;

    cin >> T;

    for (int t = 0; t < T; t++)
    {
        string str;

        cin >> str;

        int score = 0;
        int temp = 0;

        for (int i = 0; i < str.length(); i++)
        {
            if (str[i] == 'O')
            {
                temp += 1;
            }
            else
            {
                temp = 0;
            }

            score += temp;
        }

        cout << score << "\n";
    }
}