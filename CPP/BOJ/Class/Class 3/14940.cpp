// Silver 1. Easy Shortest Distance
// 44ms

#include <iostream>
#include <queue>

using namespace std;

int n, m;
int board[1000][1000];
int visited[1000][1000];

int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

void bfs(int i, int j)
{
    queue<pair<int, int>> que;
    que.push({i, j});
    
    while (!que.empty())
    {
        int r = que.front().first;
        int c = que.front().second;
        que.pop();

        for (int d = 0; d < 4; d++)
        {
            int nr = r + dr[d];
            int nc = c + dc[d];

            if (nr < 0 || nr >= n || nc < 0 || nc >= m)
                continue;

            if (!visited[nr][nc] && board[nr][nc] == 1)
            {
                visited[nr][nc] = visited[r][c] + 1;
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

    cin >> n >> m;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> board[i][j];
    
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (board[i][j] == 2)
                bfs(i, j);
    
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
            if (board[i][j] == 1 && !visited[i][j])
                cout << -1 << ' ';
            else
                cout << visited[i][j] << ' ';

        cout << '\n';
    }
}