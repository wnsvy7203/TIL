// Silver 1. Kevin Bacon's Six-Step Rule

#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <queue>
#define MAX 500000

using namespace std;

int N, M;
int visited[101];

vector<int> graph[101];

int bfs(int n)
{
    queue<int> que;
    visited[n] = 1;
    que.push(n);

    while (!que.empty())
    {
        int front = que.front();
        que.pop();

        for (int i = 0; i < graph[front].size(); i++)
        {
            if (!visited[graph[front][i]])
            {
                visited[graph[front][i]] == visited[front] + 1;
                que.push(graph[front][i]);
            }
        }
    }

    return accumulate(visited, visited+N, 0) - N - visited[n];
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;

    int u, v;

    for (int i = 0; i < M; i++)
    {
        cin >> u >> v;

        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    int min = MAX;

    for (int i = 1; i <= N; i++)
    {
        int tmp = bfs(i);
        if (min > tmp)
            min = tmp;
    }

    cout << min;
}