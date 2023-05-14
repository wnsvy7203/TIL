// Bronze 3. "Move to Center" Algorithm

#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int N;
    int x = 2;

    cin >> N;

    cout << (int)pow((pow(2, N) + 1), 2);

    while (N--)
    {
        x += x - 1;
    }

    x *= x;

    cout << x;
}