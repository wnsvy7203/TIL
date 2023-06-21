// Silver 1. Searching Maze

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N, M;
int maze[101][101] = {0, };
int visited[101][101] = {0, };
string nums;
queue<pair<int, int>> que;

int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};

int bfs()
{
    que.push(make_pair(1, 1));

    while (!que.empty())
    {
        int r = que.front().first;
        int c = que.front().second;
        que.pop();

        if (r == N && c == M)
            break;

        for (int d = 0; d < 4; d++)
        {
            int nr = r + dr[d];
            int nc = c + dc[d];

            if (nr <= 0 || nr > N || nc <= 0 || nc > M)
                continue;
            
            if (!visited[nr][nc] && maze[nr][nc])
            {
                visited[nr][nc] = visited[r][c] + 1;
                que.push(make_pair(nr, nc));
            }
        }
    }

    return visited[N][M];
}

int main()
{
    cin >> N >> M;
    visited[1][1] = 1;

    for (int i = 1; i <= N; i++)
    {
        cin >> nums;

        for (int j = 1; j <= M; j++)
            maze[i][j] = nums[j-1]-48;
    }

    cout << bfs();
}