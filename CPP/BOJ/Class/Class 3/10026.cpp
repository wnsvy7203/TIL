// Gold 5. Red-Green Color Weakness

#include <iostream>
#include <stack>
#include <cstring>

using namespace std;

int N;
char grid[100][100];
bool visited[100][100];

int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

stack<pair<int, int>> stk;

void dfs(int i, int j)
{
    stk.push({i, j});
    
    while (!stk.empty())
    {
        int r = stk.top().first;
        int c = stk.top().second;
        stk.pop();

        visited[r][c] = 1;
        
        for (int d = 0; d < 4; d++)
        {
            int nr = r + dr[d];
            int nc = c + dc[d];

            if (nr < 0 || nr >= N || nc < 0 || nc >= N)
                continue;

            if (grid[nr][nc] == grid[r][c] && !visited[nr][nc])
                stk.push({nr, nc});
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        string str;

        cin >> str;

        for (int j = 0; j < N; j++)
            grid[i][j] = str[j];
    }

    int cnt = 0;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (grid[i][j] == 'R' && !visited[i][j])
            {
                cnt++;
                dfs(i, j);
            }
            else if (grid[i][j] == 'B' && !visited[i][j])
            {
                cnt++;
                dfs(i, j);
            }
            else if (grid[i][j] == 'G' && !visited[i][j])
            {
                cnt++;
                dfs(i, j);
            }
        }
    }

    int cnt_weak = 0;
    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            if (grid[i][j] == 'G')
                grid[i][j] = 'R';
    
    memset(visited, 0, sizeof(visited));
    
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (grid[i][j] == 'R' && !visited[i][j])
            {
                cnt_weak++;
                dfs(i, j);
            }
            else if (grid[i][j] == 'B' && !visited[i][j])
            {
                cnt_weak++;
                dfs(i, j);
            }
        }
    }
    
    cout << cnt << ' ' << cnt_weak;
}