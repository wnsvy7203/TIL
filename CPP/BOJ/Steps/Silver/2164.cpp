// Silver 4. Card 2
// 4ms

#include <iostream>
#include <queue>

using namespace std;

int main()
{
    int N;

    cin >> N;

    queue<int> que;

    for (int i = 1; i <= N; i++)
    {
        que.push(i);
    }

    while (que.size() != 1)
    {
        que.pop();

        int front = que.front();

        que.pop();
        que.push(front);
    }

    cout << que.front();
}