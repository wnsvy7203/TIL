// Bronze 2. Flip Basket

#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int N, M;

    cin >> N >> M;

    int basket[105];

    for (int i = 1; i <= N; i++)
    {
        basket[i] = i;
    }

    for (int i = 0; i < M; i++)
    {
        int a, b;

        cin >> a >> b;

        for (int j = a; j <= (a+b) / 2; j++)
        {
            swap(basket[j], basket[a+b - j]);
        }
    }

    for (int i = 1; i <= N; i++)
    {
        cout << basket[i] << " ";
    }
}