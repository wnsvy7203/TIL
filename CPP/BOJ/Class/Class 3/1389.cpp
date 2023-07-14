// Silver 1. Kevin Bacon's Six-Step Rule

#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>
#include <queue>
#define MAX 101

using namespace std;

int N, M;
vector<int> graph[101];

int bfs(int n)
{
    int visited[101];
    fill_n(visited, 101, -1);

    queue<int> que;
    visited[n] = 0;
    que.push(n);

    while(!que.empty())
    {
        int next = que.front();
        que.pop();

        for (int i = 0; i < graph[next].size(); i++)
            if (visited[graph[next][i]] == -1)
            {
                visited[graph[next][i]] = visited[next] + 1;
                que.push(graph[next][i]);
            }
    }

    return accumulate(visited+1, visited+N+1, 0);
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

    int res = 10001;
    int ans = 0;

    for (int i = 1; i <= N; i++)
    {
        int tmp = bfs(i);

        if (res > tmp)
        {
            res = tmp;
            ans = i;
        }
    }

    cout << ans;
}