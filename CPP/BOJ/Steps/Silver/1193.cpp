// Silver 5. Finding Fraction

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    int X;

    cin >> X;

    int n = 1;

    while (1)
    {
        if (n * (n+1) / 2 >= X)
        {
            break;
        }

        n += 1;
    }

    int x = X - (n * (n-1) / 2);

    if (n % 2 != 0)
    {
        cout << n-x+1 << "/" << x;
    }
    else
    {
        cout << x << "/" << n-x+1;
    }
}