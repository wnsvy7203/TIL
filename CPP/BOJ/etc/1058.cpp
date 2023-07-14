// Silver 2. Friend

#include <iostream>
#define INF 3000

using namespace std;

int N;
int graph[51][51];

void floyd()
{
    for (int k = 0; k < N; k++)
        for (int i = 0; i < N; i++)
            for (int j = 0; j < N; j++)
                if (i == j || j == k || k == i)
                    continue;
                else if (graph[i][j] > graph[i][k] + graph[k][j])
                    graph[i][j] = graph[i][k] + graph[k][j];
}

int main()
{
    cin >> N;

    for (int i = 0; i < N; i++)
    {
        string fri;

        cin >> fri;

        for (int j = 0; j < N; j++)
            if (i == j)
                graph[i][j] = 0;
            else if (fri[j] == 'Y')
                graph[i][j] = 1;
            else
                graph[i][j] = INF;
    }

    floyd();

    int res = 0;

    for (int i = 0; i < N; i++)
    {
        int cnt = 0;

        for (int j = 0; j < N; j++)
        {
            if (i == j) continue;
            else if (graph[i][j] <= 2)
                cnt++;
        }
        res = max(res, cnt);
    }

    cout << res << '\n';
}