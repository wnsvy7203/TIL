// Silver 1. Assigning Apartment Complex Number

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int N;
int apt[26][26] = {0, };

int dr[4] = {-1, 1, 0, 0};
int dc[4] = {0, 0, -1, 1};
bool visited[26][26] = {0, };

int bfs(int i, int j)
{
    queue<pair<int, int>> que;
    que.push(make_pair(i, j));

    int cnt = 1;
    
    while (!que.empty())
    {
        int r = que.front().first;
        int c = que.front().second;
        que.pop();

        for (int d = 0; d < 4; d++)
        {
            int nr = r + dr[d];
            int nc = c + dc[d];

            if (nr <= 0 || nr > N || nc <= 0 || nc > N)
                continue;

            if (!visited[nr][nc] && apt[nr][nc])
            {
                visited[nr][nc] = 1;
                cnt++;
                que.push(make_pair(nr, nc));
            }
        }
    }

    return cnt;
}

int main()
{
    cin >> N;

    for (int i = 1; i <= N; i++)
    {
        string str;

        cin >> str;

        for (int j = 1; j <= N; j++)
            apt[i][j] = str[j-1]-48;
    }

    vector<int> complex;

    for (int i = 1; i <= N; i++)
        for (int j = 1; j <= N; j++)
            if (!visited[i][j] && apt[i][j])
            {
                visited[i][j] = 1;
                complex.push_back(bfs(i, j));
            }
    
    sort(complex.begin(), complex.end());

    cout << complex.size() << '\n';

    for (int i = 0; i < complex.size(); i++)
        cout << complex[i] << '\n';
}