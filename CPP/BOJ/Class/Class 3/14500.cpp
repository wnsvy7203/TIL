// Gold 4. Tetronomino
// 16ms

#include <iostream>
#include <queue>

using namespace std;

int N, M, ans, num;
int paper[501][501];
int visited[501][501];

int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

void dfs(int r, int c, int cnt, int tmp)
{
    if (tmp + (num * (4-cnt)) <= ans)
        return;
    
    if (cnt == 4)
    {
        ans = max(ans, tmp);
        return;
    }
    
    for (int d = 0; d < 4; d++)
    {
        int nr = r + dr[d];
        int nc = c + dc[d];

        if (nr < 0 || nr >= N || nc < 0 || nc >= M)
            continue;
        
        if (!visited[nr][nc])
        {
            if (cnt == 2)
            {
                visited[nr][nc] = 1;
                dfs(r, c, cnt+1, tmp+paper[nr][nc]);
                visited[nr][nc] = 0;
            }

            visited[nr][nc] = 1;
            dfs(nr, nc, cnt+1, tmp+paper[nr][nc]);
            visited[nr][nc] = 0;
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;

    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
        {
            cin >> paper[i][j];

            num = max(num, paper[i][j]);
        }
    
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
        {
            visited[i][j] = 1;
            dfs(i, j, 1, paper[i][j]);
            visited[i][j] = 0;
        }
    
    cout << ans;
}