// Bronze 2. Math is Untact Course

#include <iostream>

using namespace std;

int main()
{
    double a, b, c, d, e, f;

    cin >> a >> b >> c >> d >> e >> f;

    // ax + by = c
    // dx + ey = f


    // (a*e)x + (b*e)y = c*e
    // (b*d)x + (b*e)y = b*f

    // (a*e - b*d)x = c*e - b*f
    int x = (c*e - b*f) / (a*e - b*d);

    // (a*d)x + (b*d)y = c*d
    // (a*d)x + (a*e)y = a*f

    // (b*d - a*e)y = c*d - a*f
    int y = (c*d - a*f) / (b*d - a*e);

    cout << x << " " << y;
}