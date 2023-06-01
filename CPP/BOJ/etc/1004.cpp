// Silver 3. The Little Prince

#include <iostream>
#include <cmath>

using namespace std;

int T;

int main()
{
    cin >> T;

    while (T--)
    {
        int x1, y1, x2, y2;
        int n;

        cin >> x1 >> y1 >> x2 >> y2 >> n;

        int cnt = 0;

        for (int i = 0; i < n; i++)
        {
            int cx, cy, r;

            cin >> cx >> cy >> r;

            if (pow(x1-cx, 2) + pow(y1-cy, 2) <= pow(r, 2) && pow(x2-cx, 2) + pow(y2-cy, 2) > pow(r, 2))
                cnt++;
            else if (pow(x1-cx, 2) + pow(y1-cy, 2) > pow(r, 2) && pow(x2-cx, 2) + pow(y2-cy, 2) <= pow(r, 2))
                cnt++;
        }

        cout << cnt << '\n';
    }
}