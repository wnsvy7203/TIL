#include <iostream>
#include <queue>

using namespace std;

int N;
int board[3][3];
int visited[3][3];
queue<pair<int, int>> que;

void bfs()
{
    que.push({0, 0});
    visited[0][0] = 1;

    while (!que.empty())
    {
        int r = que.front().first;
        int c = que.front().second;
        que.pop();

        int go = board[r][c];

        if (r+go < N && !visited[r+go][c])
        {
            que.push({r+go, c});
            visited[r+go][c] = 1;
        }

        if (c+go < N && !visited[r][c+go])
        {
            que.push({r, c+go});
            visited[r][c+go] = 1;
        }
    }

    if (visited[N-1][N-1])
        cout << "HaruHaru";
    else
        cout << "Hing";
}

int main()
{
    cin >> N;

    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cin >> board[i][j];
    
    bfs();
}