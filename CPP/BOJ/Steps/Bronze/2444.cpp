// Bronze 3. Stamp the Stars Out

#include <iostream>

using namespace std;

int N;

int main()
{
    cin >> N;

    for (int i = 1; i < 2 * N; i++)
    {
        if (i <= N)
        {
            for (int j = i; j < N; j++)
            {
                cout << " ";
            }
            for (int j = 1; j < 2 * i; j++)
            {
                cout << "*";
            }
            cout << "\n";
        }
        else
        {
            for (int j = 0; j < i - N; j++)
            {
                cout << " ";
            }
            for (int j = 1; j < 2 * (2 * N - i); j++)
            {
                cout << "*";
            }

            if (i != 2 * N - 1)
            {
                cout << "\n";
            }
        }
    }
}