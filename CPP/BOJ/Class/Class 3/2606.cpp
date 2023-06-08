// Silver 3. Virus

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N, E;
vector<int> graph[101];
bool visited[101] = {0, };
queue<int> que;

int bfs(int v)
{
    int cnt = -1;

    que.push(v);
    visited[v] = 1;

    while (!(que.empty()))
    {
        int w = que.front();
        que.pop();
        cnt++;

        for (int i = 0; i < graph[w].size(); i++)
        {
            if (!visited[graph[w][i]])
            {
                visited[graph[w][i]] = 1;
                que.push(graph[w][i]);
            }
        }
    }

    return cnt;
}

int main()
{
    cin >> N >> E;

    while (E--)
    {
        int u, v;

        cin >> u >> v;

        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    cout << bfs(1);
}