// Silver 5. LCM

#include <iostream>

using namespace std;

int gcd(long long int a, long long int b)
{
    while (b != 0)
    {
        long long int r = a % b;
        a = b;
        b = r;
    }

    return a;
}

int main()
{
    long long int A, B;

    cin >> A >> B;

    cout << A * B / gcd(A, B);
}