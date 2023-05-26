// Bronze 2. Recursion Master
// 164ms

// 재귀 함수의 호출 횟수

#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T;

    cin >> T;

    while (T--)
    {
        int cnt = 0;

        bool flag = 1;

        string str;

        cin >> str;

        for (int i = 0; i <= str.length() / 2; i++)
        {
            cnt++;

            if (str[i] != str[str.length()-1-i])
            {
                flag = 0;
                break;
            }
        }

        cout << flag << ' ' << cnt << '\n';
    }
}