// Bronze 2. 문자열 반복

#include <iostream>
#include <string>

using namespace std;


int main()
{
    int T;

    cin >> T;


    for (int t = 0; t < T; t++)
    {
        int R;
        string S;

        cin >> R >> S;

        for (int i = 0; i < S.length(); i++)
        {
            for (int j = 0; j < R; j++)
            {
                cout << S[i];
            }
        }
        cout << "\n";
    }
}