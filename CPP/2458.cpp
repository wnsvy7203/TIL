// Gold 4. Tall Order

#include <iostream>
#define INF 501

using namespace std;

int N, M;
int graph[501][501];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;

    for (int i = 1; i <= N; i++)
        for (int j = 1; j <= N; j++)
            if (i != j)
                graph[i][j] = INF;

    int a, b;

    for (int i = 0; i < M; i++)
    {
        cin >> a >> b;

        graph[a][b] = 1;
    }
}