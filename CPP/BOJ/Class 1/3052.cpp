// Bronze 2

#include <iostream>

using namespace std;

int main()
{
    int N;

    int remain[42] = {};

    for (int i = 0; i < 10; i++)
    {
        cin >> N;

        remain[N % 42]++;
    }

    int cnt = 0;

    for (int i = 0; i < 42; i++)
    {
        if (remain[i] != 0)
        {
            cnt++;
        }
    }

    cout << cnt;
}