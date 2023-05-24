// Silver 3. Fraction Sum

#include <iostream>

using namespace std;

int gcd(int a, int b)
{
    while (b)
    {
        int temp = a % b;
        a = b;
        b = temp;
    }

    return a;
}

int main()
{
    int a, b, c, d;

    cin >> a >> b >> c >> d;

    int r = gcd(b, d);
    int g = gcd(a * d + c * b, b * d);

    cout << (a * d + c * b) / g << " " << b * d / g;
}