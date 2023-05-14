// Bronze 3. Laundromat Owner
// 20ms

#include <iostream>
#include <vector>

using namespace std;

int T;

int main()
{
    cin >> T;

    for (int t = 0; t < T; t++)
    {
        int n;

        cin >> n;

        cout << n / 25 << " ";

        n -= 25 * (n / 25);

        cout << n / 10 << " ";

        n -= 10 * (n / 10);

        cout << n / 5 << " ";

        n -= 5 * (n / 5);

        cout << n << "\n";
    }
}