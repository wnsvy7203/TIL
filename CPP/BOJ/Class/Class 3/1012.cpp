// Silver 2. Organic Cabbage

#include <iostream>
#include <vector>
#include <queue>

using namespace std;
int T;
int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};
int N, M, K;
int cnt = 0;
bool visited[50][50] = {0, };
vector<vector<int>> cabbage(50, vector<int>(50, 0));

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
            
            if (cabbage[nr][nc] && !visited[nr][nc])
            {
                visited[nr][nc] = 1;
                que.push(make_pair(nr, nc));
            }
        }
    }
}

int main()
{
    cin >> T;

    while (T--)
    {
        cnt = 0;
        for (int i = 0; i < 50; i++)
            for (int j = 0; j < 50; j++)
            {
                cabbage[i][j] = 0;
                visited[i][j] = 0;
            }

        cin >> M >> N >> K;

        for (int i = 0; i < K; i++)
        {
            int X, Y;

            cin >> X >> Y;

            cabbage[Y][X] = 1;
        }

        for (int i = 0; i < N; i++)
            for (int j = 0; j < M; j++)
                if (cabbage[i][j] && !visited[i][j])
                {
                    que.push(make_pair(i, j));
                    cnt++;
                    bfs();

                }
        
        cout << cnt << '\n';
    }
}