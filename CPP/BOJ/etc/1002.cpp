// Silver 3. Turret
// 원의 접점의 개수를 구하는 문제

#include <iostream>
#include <cmath>

using namespace std;

int T;

int main()
{
    cin >> T;

    while (T--)
    {
        int x1, y1, r1, x2, y2, r2;

        cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;

        double dist = sqrt(pow((x1-x2), 2) + pow((y1-y2), 2));

        if (!dist)
        {
            if (r1 == r2) cout << -1 << '\n';
            else cout << 0 << '\n';
        }
        else
        {
            if (r1 + r2 > dist && abs(r1-r2) < dist)
                cout << 2 << '\n';
            else if (r1 + r2 == dist || abs(r1-r2) == dist)
                cout << 1 << '\n';
            else
                cout << 0 << '\n';
        }
    }
}