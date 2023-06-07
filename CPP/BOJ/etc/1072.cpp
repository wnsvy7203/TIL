// Silver 3. Game

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    long long int X, Y;

    cin >> X >> Y;

    int Z = Y * 100 / X;

    if (Z >= 99)
    {
        cout << -1;
        return 0;
    }

    int start = 0;
    int end = 1000000000;

    while (start <= end)
    {
        int mid = (start + end) / 2;
        int temp = (Y+mid) * 100 / (X+mid);

        if (Z >= temp) start = mid + 1;
        else end = mid - 1;
    }

    cout << end+1;
}