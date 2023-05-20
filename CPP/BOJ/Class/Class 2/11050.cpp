// Bronze 1. Binomial Coefficient

#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int N, K;

    cin >> N >> K;

    int ans = 1;
    int div = 1;

    for (int i = 0; i < K; i++)
    {
        ans *= (N - i);
        div *= (K - i);
    }

    cout << ans / div;
}