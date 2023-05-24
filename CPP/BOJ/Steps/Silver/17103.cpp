// Silver 2. Goldbach Partition
// 56ms

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

vector<bool> prime(1000001, 1);

void prime_check()
{
    prime[0] = 0;
    prime[1] = 0;

    for (int i = 2; i < sqrt(prime.size())+1; i++)
    {
        if (prime[i])
        {
            for (int j = 2; i * j <= prime.size(); j++)
            {
                prime[i * j] = 0;
            }
        }
    }
}

int Goldbach(int n)
{
    int cnt = 0;

    for (int j = 2; j <= n/2; j++)
    {
        if (prime[j] == 1 && prime[n-j] == 1)
        {
            cnt++;
        }
    }

    return cnt;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int T;

    cin >> T;

    prime_check(); 

    for (int t = 0; t < T; t++)
    {
        int n;

        cin >> n;

        cout << Goldbach(n) << '\n';
    }
}