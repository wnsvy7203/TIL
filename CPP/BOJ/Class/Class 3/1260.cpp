// Silver 2. DFS and BFS

#include <iostream>
#include <stack>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int N, M, V;
stack<int> stk;
queue<int> que;
vector<int> adjList[1001];
bool visited[1001] = {0, };
stack<int> res_stk;
queue<int> res_que;

void dfs(int v)
{
    stk.push(v);

    while (!stk.empty())
    {
        int top = stk.top();
        stk.pop();

        if (visited[top]) continue;
        
        visited[top] = 1;
        cout << top << ' ';

        for (int i = adjList[top].size()-1; i >= 0; i--)
            stk.push(adjList[top][i]);
    }
}

void bfs(int v)
{
    que.push(v);

    while (!que.empty())
    {
        int front = que.front();
        que.pop();

        if (visited[front]) continue;

        visited[front] = 1;
        cout << front << ' ';

        for (int i = 0; i < adjList[front].size(); i++)
            que.push(adjList[front][i]);
    }
}

int main()
{
    cin >> N >> M >> V;

    for (int i = 0; i < M; i++)
    {
        int u, v;

        cin >> u >> v;

        adjList[u].push_back(v);
        adjList[v].push_back(u);
    }

    for (int i = 1; i <= N; i++)
        sort(adjList[i].begin(), adjList[i].end());

    dfs(V);
    cout << '\n';

    for (int i = 0; i < 1001; i++)
        visited[i] = 0;

    bfs(V);
}
