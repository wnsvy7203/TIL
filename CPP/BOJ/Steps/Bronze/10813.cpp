// Bronze 2. Changing Balls

#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int N, M;

    cin >> N >> M;

    int baskets[105] = {};

    for (int i = 1; i <= N; i++)
    {
        baskets[i] = i;
    }

    for (int i = 0; i < M; i++)
    {
        int a, b;

        cin >> a >> b;

        swap(baskets[a], baskets[b]);
    }

    for (int i = 1; i <= N; i++)
    {
        cout << baskets[i] << " ";
    }
}