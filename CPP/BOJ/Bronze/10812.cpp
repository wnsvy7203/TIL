// Bronze 2. Changing Order of Baskets

#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int N, M;

    cin >> N >> M;

    int basket[105] = {};

    for (int i = 1; i <= N; i++)
    {
        basket[i] = i;
    }

    for (int i = 0; i < M; i++)
    {
        int a, b, c;

        cin >> a >> b >> c;
        
        rotate(basket + a, basket + c, basket + b+1);
    }

    for (int i = 1; i <= N; i++)
    {
        cout << basket[i] << " ";
    }
}
