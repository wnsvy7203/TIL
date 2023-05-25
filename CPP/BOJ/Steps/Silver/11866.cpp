// Silver 5. Josephus Problem 0

#include <iostream>
#include <queue>

using namespace std;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N, K;

    cin >> N >> K;

    queue<int> que;

    for (int i = 1; i <= N; i++)
    {
        que.push(i);
    }

    cout << '<';

    while (!que.empty())
    {
        for (int i = 1; i < K; i++)
        {
            int f = que.front();
            que.pop();
            que.push(f);
        }

        int front = que.front();

        if (que.size() == 1)
        {
            cout << front;
            break;
        }
        else
        {
            cout << front << ", ";
            que.pop();
        }
    }

    cout << '>';
}