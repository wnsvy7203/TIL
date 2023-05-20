// Bronze 2. Decomposition Sum
// 8ms

#include <iostream>

using namespace std;

int N;

int main()
{
    cin >> N;

    bool check = 0;

    for (int i = 1; i <= N; i++)
    {
        int n = i;
        int num = i;

        while (n != 0)
        {
            num += n % 10;
            n /= 10;
        }

        if (num == N)
        {
            check = 1;
            cout << i;
            break;
        }
    }

    if (check == 0)
    {
        cout << (int)check;
    }
}