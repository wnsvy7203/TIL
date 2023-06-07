// Silver 1. Easy Fastest Way
// 84ms

#include <iostream>
#include <queue>

using namespace std;

int land[1001][1001] = {0, };
int visited[1001][1001] = {0, };

int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};
int n, m;

queue<pair<int, int>> que;

void bfs()
{
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
            
            if (!visited[nr][nc] && land[nr][nc])
            {
                visited[nr][nc] = visited[r][c] + 1;
                que.push(make_pair(nr, nc));
            }
        }
    }
}

int main()
{
    cin >> n >> m;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> land[i][j];

    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            if (land[i][j] == 2)
            {
                que.push(make_pair(i, j));
                visited[i][j] = 1;
            }

    bfs();

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
            if (land[i][j] == 1 && !visited[i][j])
                cout << -1 << ' ';
            else if (!land[i][j])
                cout << 0 << ' ';
            else
                cout << visited[i][j]-1 << ' ';
        cout << '\n';
    }
}
