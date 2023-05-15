// Bronze 1. Factorization
// 32ms

#include <iostream>

using namespace std;

int main()
{
    int N;

    cin >> N;

    int cnt(2);

    while (1)
    {
        if (N % cnt == 0)
        {
            cout << cnt << '\n';
            N /= cnt;
        }
        else
        {
            cnt += 1;
        }

        if (N == 1)
        {
            break;
        }
    }
}