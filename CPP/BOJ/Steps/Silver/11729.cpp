// Silver 1. Hanoi's Tower Moving Order
// 176ms

#include <iostream>
#include <vector>

using namespace std;

int N;

void hanoi(int n, int start, int end, int mid)
{
    if (n == 1)
        cout << start << ' ' << end << '\n';
    else
    {
        hanoi(n-1, start, mid, end);
        cout << start << ' ' << end << '\n';
        hanoi(n-1, mid, end, start);
    }
}

int main()
{
    cin >> N;

    cout << (1 << N)-1 << '\n';

    hanoi(N, 1, 3, 2);
}