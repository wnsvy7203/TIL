// Bronze 3. Goal In

#include <iostream>

using namespace std;

int N, M;

int main()
{
    cin >> N >> M;

    int basket[105] = {};

    for (int i = 0; i < M; i++)
    {
        int a, b, c;

        cin >> a >> b >> c;

        for (int j = a; j <= b; j++)
        {
            basket[j] = c;
        }
    }

    for (int i = 1; i <= N; i++)
    {
        cout << basket[i] << " ";
    }
}