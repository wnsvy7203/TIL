// Silver 1. ABS Heap
// 16ms

#include <iostream>
#include <queue>

using namespace std;

int N;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    priority_queue<pair<int, int>> pque;
    
    cin >> N;

    while (N--)
    {
        int x;

        cin >> x;

        if (x)
            pque.push(make_pair(-abs(x), -x));
        else
        {
            if (pque.empty())
                cout << 0 << '\n';
            else
            {
                cout << -pque.top().second << '\n';
                pque.pop();
            }
        }
    }
}