// Gold 4. DSLR
// 5420ms

#include <iostream>
#include <queue>
#include <cstring>

using namespace std;

int T, s, e;
bool visited[10000];

void bfs()
{
    cout.tie(0);
    
    queue<pair<int, string>> que;
    que.push({ s, "" });

    while (!que.empty())
    {
        int front = que.front().first;
        string second = que.front().second;
        que.pop();

        if (front == e)
        {
            cout << second << '\n';
            return;
        }

        int dfront = 2*front%10000;
        string dsecond = second+'D';

        if (!visited[dfront])
        {
            visited[dfront] = 1;
            que.push({ dfront, dsecond });
        }

        int sfront = front-1 < 0 ? 9999 : front-1;
        string ssecond = second+'S';

        if (!visited[sfront])
        {
            visited[sfront] = 1;
            que.push({ sfront, ssecond });
        }

        int divL = front / 1000;
        int modL = front % 1000;

        int lfront = modL * 10 + divL;
        string lsecond = second+'L';

        if (!visited[lfront])
        {
            visited[lfront] = 1;
            que.push({ lfront, lsecond });
        }

        int divR = front / 10;
        int modR = front % 10;

        int rfront = modR * 1000 + divR;
        string rsecond = second+'R';

        if (!visited[rfront])
        {
            visited[rfront] = 1;
            que.push({ rfront, rsecond });
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> T;

    while (T--)
    {
        cin >> s >> e;

        memset(visited, 0, sizeof(visited));
        bfs();
    }
}