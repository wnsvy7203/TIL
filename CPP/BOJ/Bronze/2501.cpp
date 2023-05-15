// Bronze 3. Calculating Divisors

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int N, K;

    cin >> N >> K;

    vector<int> div;

    for (int i = 1; i <= N; i++)
    {
        if (N % i == 0)
        {
            div.push_back(i);
        }
    }

    if (div.size() < K)
    {
        cout << 0;
    }
    else
    {
        cout << div[K-1];
    }
}