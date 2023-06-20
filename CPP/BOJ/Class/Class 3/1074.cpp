// Silver 1. Z

#include <iostream>
#include <cmath>

using namespace std;

int n, r, c;

void Z(int num, int i, int j, int n)
{
    if (i == r && j == c)
        cout << num;
    else if (r < i+n/2 && c < j+n/2)
        Z(num, i, j, n/2);
    else if (r < i+n/2 && c >= j+n/2)
    {
        num += pow(n/2, 2);
        Z(num, i, j+n/2, n/2);
    }
    else if (r >= i+n/2 && c < j+n/2)
    {
        num += pow(n/2, 2) * 2;
        Z(num, i+n/2, j, n/2);
    }
    else if (r >= i+n/2 && c >= j+n/2)
    {
        num += pow(n/2, 2) * 3;
        Z(num, i+n/2, j+n/2, n/2);
    }
}

int main()
{
    cin >> n >> r >> c;

    int N = pow(2, n);

    Z(0, 0, 0, N);
}