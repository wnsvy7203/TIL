// Gold 4. Floyd
// 28ms

#include <iostream>
#define INF 10000000

using namespace std;

int n, m;
int graph[101][101];

void floyd()
{
    for (int k = 1; k <= n; k++)
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                if (i == j || j == k || k == i)
                    continue;
                else if (graph[i][j] > graph[i][k] + graph[k][j])
                    graph[i][j] = graph[i][k] + graph[k][j];
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> n >> m;

    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
        {
            if (i == j)
                graph[i][j] = 0;
            else
                graph[i][j] = INF;
        }

    int a, b, c;

    for (int i = 0; i < m; i++)
    {
        cin >> a >> b >> c;

        graph[a][b] = min(graph[a][b], c);
    }

    floyd();

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            if (graph[i][j] == INF)
                cout << 0 << ' ';
            else
               cout << graph[i][j] << ' ';
        }
        cout << '\n';
    }
}