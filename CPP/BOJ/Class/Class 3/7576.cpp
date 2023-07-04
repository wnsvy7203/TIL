// Gold 5. Tomato
// 80ms

#include <iostream>
#include <queue>

using namespace std;

int M, N;
int tomato[1001][1001];
bool visited[1001][1001];

int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

queue<pair<int, int>> que;

void bfs()
{
    while (!que.empty())
    {
        int r = que.front().first;
        int c = que.front().second;
        que.pop();

        visited[r][c] = 1;

        for (int d = 0; d < 4; d++)
        {
            int nr = r + dr[d];
            int nc = c + dc[d];

            if (nr < 0 || nr >= N || nc < 0 || nc >= M)
                continue;
            
            if (tomato[nr][nc] == 0)
            {
                tomato[nr][nc] = tomato[r][c] + 1;
                que.push({nr, nc});
            }
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> M >> N;

    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
        {
            cin >> tomato[i][j];
            
            if (tomato[i][j] == 1 && !visited[i][j])
                que.push({i, j});
        }
    
    bfs();

    int res = 0;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
        {
            if (!tomato[i][j])
            {
                cout << -1;
                return 0;
            }

            res = max(res, tomato[i][j]);
        }
    
    cout << res-1;
}