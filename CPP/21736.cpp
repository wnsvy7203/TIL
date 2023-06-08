// Silver 2. Sophomores Need Friends
// 24ms

#include <iostream>
#include <queue>

using namespace std;

int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};
int N, M;

char campus[601][601] = {' ', };
bool visited[601][601] = {0, };
queue<pair<int, int>> que;
int cnt = 0;

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

            if (nr < 0 || nr >= N || nc < 0 || nc >= M || campus[nr][nc] == 'X')
                continue;
            
            if (!visited[nr][nc])
            {
                visited[nr][nc] = 1;
                que.push(make_pair(nr, nc));

                if (campus[nr][nc] == 'P')
                    cnt++;
            }
        }
    }
}

int main()
{
    cin >> N >> M;

    string str;

    for (int i = 0; i < N; i++)
    {
        cin >> str;

        for (int j = 0; j < M; j++)
            campus[i][j] = str[j];
    }

    for (int i = 0; i < N; i++)
        for (int j = 0 ; j < M; j++)
            if (campus[i][j] == 'I')
            {
                que.push(make_pair(i, j));
                visited[i][j] = 1;
            }
    
    bfs();

    if (cnt) cout << cnt;
    else cout << "TT";
}

