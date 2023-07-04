// Gold 5. Tomato
// 100ms

#include <iostream>
#include <tuple>
#include <queue>
#include <cstring>
#define MAX 1000000

using namespace std;

int M, N, H;
int dh[6] = {-1, 1, 0, 0, 0, 0};
int dr[6] = {0, 0, -1, 1, 0, 0};
int dc[6] = {0, 0, 0, 0, -1, 1};

int tomato[101][101][101];
bool visited[101][101][101];
queue<tuple<int, int, int>> que;

void bfs()
{
    while (!que.empty())
    {
        int h = get<0>(que.front());
        int r = get<1>(que.front());
        int c = get<2>(que.front());
        que.pop();

        visited[h][r][c] = 1;

        for (int d = 0; d < 6; d++)
        {
            int nh = h + dh[d];
            int nr = r + dr[d];
            int nc = c + dc[d];

            if (nr < 0 || nr >= N || nc < 0 || nc >= M || nh < 0 || nh >= H)
                continue;
            
            if (!tomato[nh][nr][nc])
            {
                tomato[nh][nr][nc] = tomato[h][r][c] + 1;
                que.push({nh, nr, nc});
            }
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> M >> N >> H;

    for (int i = 0; i < H; i++)
        for (int j = 0; j < N; j++)
            for (int k = 0; k < M; k++)
            {
                cin >> tomato[i][j][k];

                if (tomato[i][j][k] == 1 && !visited[i][j][k])
                    que.push({i, j, k});
            }
    
    bfs();

    int res = 0;
    for (int i = 0; i < H; i++)
        for (int j = 0; j < N; j++)
        {
            for (int k = 0; k < M; k++)
            {
                if (tomato[i][j][k] == 0)
                {
                    cout << -1;
                    exit(0);
                }
                else 
                    res = max(res, tomato[i][j][k]);
            }
        }

    cout << res-1;
}