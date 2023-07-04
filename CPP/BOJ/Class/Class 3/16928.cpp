// Gold 5. Snake and Ladder Game

#include <iostream>
#include <vector>
#include <queue>
#define MAX 105

using namespace std;

int N, M, u, v;
int visited[101];
int graph[101];
queue<int> que;

void bfs()
{
    while (!que.empty())
    {
        int front = que.front();
        que.pop();

        for (int i = 1; i <= 6; i++)
        {
            int nfront = front + i;

            if (nfront > 100)
                continue;

            if (!visited[nfront])
            {
                int tmp = graph[nfront];

                if (!visited[tmp])
                {
                    que.push(tmp);
                    visited[tmp] = visited[front] + 1;
                }

                if (tmp == 100)
                    return;
            }
        }
    }
}

int main()
{
    cin >> N >> M;

    for (int i = 1; i < 101; i++)
        graph[i] = i;

    for (int i = 0; i < N+M; i++)
    {
        cin >> u >> v;
        graph[u] = v;
    }

    que.push(1);
    visited[1] = 1;

    bfs();

    cout << visited[100]-1;
}