// Silver 3. Ailing Knight

#include <iostream>
#include <stack>

using namespace std;

int N, M;

int main()
{
    cin >> N >> M;

    if (N == 1) cout << 1;
    else if (N == 2) cout << min(4, (M-1) / 2 + 1);
    else
    {
        if (M >= 7) cout << M-2;
        else cout << min(4, M);
    }
}