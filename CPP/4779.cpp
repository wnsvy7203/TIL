// Silver 3. Cantorian Set
// 44ms

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int N;

void Canto(int n)
{
    int size = pow(3, n-1);

    if (!n)
    {
        cout << '-';
        return;
    }

    Canto(n-1);
    for (int i = 0; i < size; i++)
        cout << ' ';
    Canto(n-1);
}

int main()
{
    while(cin >> N)
    {
        Canto(N);
        cout << '\n';
    }
}