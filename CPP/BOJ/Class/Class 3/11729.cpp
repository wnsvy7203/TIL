// Silver 2. Max Heap
// 16ms

#include <iostream>
#include <queue>

using namespace std;

priority_queue<int> pque;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N;

    while (N--)
    {
        int num;
        cin >> num;

        if (num)
            pque.push(num);
        else
            if (pque.empty()) cout << 0 << '\n';
            else
            {
                cout << pque.top() << '\n';
                pque.pop();
            }
    }
}