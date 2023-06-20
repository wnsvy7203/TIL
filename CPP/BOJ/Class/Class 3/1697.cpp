// Silver 1. Hide and Seek

#include <iostream>
#include <queue>

using namespace std;

int N, K;
int visited[100001] = {0, };

int bfs(int n, int k)
{
    queue<int> que;
    que.push(n);
    visited[n] = 1;

    int ans = 0;

    while (!que.empty())
    {
        int front = que.front();
        que.pop();

        if (front == k)
        {
            ans = visited[k];
            break;
        }

        for (int i = 0; i < 3; i++)
        {
            if (front-1 >= 0 && !visited[front-1])
            {
                visited[front-1] = visited[front]+1;
                que.push(front-1);
            }

            if (front+1 <= 100000 && !visited[front+1])
            {
                visited[front+1] = visited[front]+1;
                que.push(front+1);
            }

            if (front*2 <= 100000 && !visited[front*2])
            {
                visited[front*2] = visited[front]+1;
                que.push(front*2);
            }
        }
    }

    return ans;
}

int main()
{
    cin >> N >> K;

    cout << bfs(N, K)-1;
}
