// Silver 3. N and M(3)
// 492ms

#include <iostream>
#include <vector>
#include <algorithm>

#define MAX 9

using namespace std;

int N, M;
vector<int> per(MAX, 0);
vector<int> visited(MAX, 0);

void dfs(int cnt)
{
    if (cnt == M)
    {
        for (int i = 0; i < M; i++)
            cout << per[i] << ' ';
        
        cout << '\n';
        return;
    }

    for (int i = 1; i <= N; i++)
    {
        if (visited[i] <= M)
        {
            visited[i]++;
            per[cnt] = i;
            dfs(cnt+1);
            visited[i]--;
        }
    }
}

int main()
{
    cin >> N >> M;

    dfs(0);
}