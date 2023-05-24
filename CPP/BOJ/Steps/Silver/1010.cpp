// Silver 5. Building Bridge

#include <iostream>

using namespace std;

int main()
{
    int T;

    cin >> T;

    for (int t = 0; t < T; t++)
    {
        int N, M;

        cin >> N >> M;

        long long int cnt = 1;

        for (int i = M; i > M-N; i--)
        {
            cnt *= i;
        }

        for (int i = N; i > 0; i--)
        {
            cnt /= i;
        }

        cout << cnt << '\n';
    }
}