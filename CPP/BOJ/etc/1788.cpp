// Silver 3. the Expansion of Fibonacci Num

#include <iostream>
#define MOD 1000000000
#define MAX 1000001

using namespace std;

int n;
long long int memo[MAX];

int main()
{
    cin >> n;

    int flag = 1;

    if (n < 0)
    {
        n *= -1;
        if (!(n%2))
            flag = -1;
    }
    else if (n == 0)
        flag = 0;

    memo[0] = 0;
    memo[1] = 1;

    for (int i = 2; i < MAX; i++)
        memo[i] = (memo[i-1] + memo[i-2]) % MOD;
    
    cout << flag << '\n' << memo[n];
}