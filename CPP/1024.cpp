// Silver 2. Sum of Sequence

#include <iostream>

using namespace std;

int N, L;

int main()
{
    cin >> N >> L;

    int s = -1;
    int e = -1;

    while (L <= 100)
    {
        if (!(L%2))
        {
            if (N%L == L/2)
            {
                s = N/L - L/2 + 1;
                e = N/L + L/2;
                break;
            }
        }
        else
        {
            if (!(N%L))
            {
                s = N/L - L/2;
                e = N/L + L/2;
                break;
            }
        }

        L++;
    }

    if (s < 0)
        cout << -1;
    else
    {
        for (int i = s; i <= e; i++)
            cout << i << ' ';
    }
}