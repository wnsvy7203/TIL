// Silver 4. Sugar Delivery

#include <iostream>

using namespace std;

int main()
{
    int N;

    cin >> N;

    int a = 0;
    int b = 0;
    int n = N;

    if (!(N % 5))
    {
        a = N / 5;
        cout << a;
        return 0;
    }

    while (n > 0)
    {
        b++;
        n = N - 3*b;

        if (n && !(n % 5))
        {
            a = n / 5;
            cout << a+b;
            return 0;
        }
    }

    if (!n) cout << b;
    else if (n < 0) cout << -1;
}