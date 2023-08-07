// 36ms

#include <iostream>
#include <queue>
#include <cstring>

using namespace std;

int n, m, q;
vector<int> graph[1001];
int visited[1001];

queue<int> que;

void bfs()
{
    memset(visited, 0, sizeof(visited));
    que.push(1);
    visited[1] = 1;

    while (!que.empty())
    {
        int f = que.front();
        que.pop();

        for (int x = 0; x < graph[f].size(); x++)
            if (!visited[graph[f][x]])
            {
                que.push(graph[f][x]);
                visited[graph[f][x]] = visited[f] + 1;
            }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;

    int u, v;

    while (m--)
    {
        cin >> u >> v;

        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    cin >> q;

    int i, j;

    while (q--)
    {
        cin >> i >> j;

        graph[i].push_back(j);
        graph[j].push_back(i);

        bfs();

        for (int i = 1; i <= n; i++)
            cout << visited[i] - 1 << ' ';

        cout << '\n';
    }
}