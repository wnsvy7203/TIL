// Silver 1. Find Route

#include <iostream>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;

int N;
bool visited[100] = {0, };
vector<int> graph[100];
queue<int> que;

void bfs(int i)
{
    que.push(i);

    while (!que.empty())
    {
        int front = que.front();
        que.pop();

        for (int i = 0; i < graph[front].size(); i++)
            if (!visited[graph[front][i]])
            {
                visited[graph[front][i]] = 1;
                que.push(graph[front][i]);
            }
    }

    for (int j = 0; j < N; j++)
        cout << visited[j] << ' ';
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N;

    int node;

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> node;

            if (node)
                graph[i].push_back(j);
        }
    }

    for (int i = 0; i < N; i++)
    {
        memset(visited, 0, sizeof(visited));
        bfs(i);

        cout << '\n';
    }
}