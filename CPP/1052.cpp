// Silver 1. Water Bottle

#include <iostream>
#include <vector>

using namespace std;

int bottle[10000001] = {1, };

int main()
{
    int N, K;
    // N <= 10,000,000
    // K <= 1,000

    cin >> N >> K;

    int n = N;

    while (1)
    {
        for (int i = 0; i < N; i += 2*K)
        {
            for (int j = i; j < N; j += K)
            {
            }
            if (i % 2)
                bottle[i]--;
            else
                bottle[i]++;
        }
    }
}