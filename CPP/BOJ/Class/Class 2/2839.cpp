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

    // n이 5의 배수가 될 때까지 3kg 봉지를 '계속' 만든다. - 반복문이 필요
    // n이 5의 배수가 되면 그만, a + b를 출력한다.
    // n이 0이 되면 b 출력
    // n이 1이나 2가 되면, -1을 출력한다.

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