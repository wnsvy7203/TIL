// Silver 1. Water Bottle

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N, K;

    cin >> N >> K;

    vector<int> bottle(N, 1);

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