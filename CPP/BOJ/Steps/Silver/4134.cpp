// Silver 4. Next Prime Number
// 232ms

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int T;

    cin >> T;

    for (int t = 0; t < T; t++)
    {
        unsigned int n;

        cin >> n;

        if (n <= 2)
        {
            cout << 2 << '\n';
            continue;
        }

        unsigned int p = n;

        while (1)
        {
            bool check = true;

            for (int i = 2; i <= sqrt(p) + 1; i++)
            {
                if (!(p % i))
                {
                    check = false;
                    break;
                }
            }

            if (check)
            {
                cout << p << '\n';
                break;
            }
            else
            {
                p += 1;
            }
        }
    }
}