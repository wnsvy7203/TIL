// Silver 3. Present

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    long long int N, L, W, H;
    double start = 0;
    double end = 0;

    cin >> N >> L >> W >> H;

    end = max(L, (max(W, H)));

    for (int i = 0; i < 10000; i++)
    {
        long double mid = (start + end) / 2;

        if (((long long)(L / mid)) * ((long long)(W / mid)) * ((long long)(H / mid)) < N) end = mid;
        else start = mid;
    }

    cout.precision(9);
    cout << fixed << start;
}