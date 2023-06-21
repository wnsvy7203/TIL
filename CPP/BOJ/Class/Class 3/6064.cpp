// Silver 1. Cain Calendar
// 472ms

#include <iostream>
#include <vector>

using namespace std;

int T;

int gcd(int a, int b)
{
    if (!b) return a;
    else return gcd(b, a%b);
}

int lcm(int a, int b)
{
    return (a*b) / gcd(a, b);
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> T;

    int M, N, x, y;

    while (T--)
    {
        int ans = -1;
        cin >> M >> N >> x >> y;
        
        while (x <= lcm(M, N))
        {
            if (x % N == y % N)
            {
                ans = x;
                break;
            }
            x += M;
        }

        cout << ans << '\n';
    }
}