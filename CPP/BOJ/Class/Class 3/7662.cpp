// Gold 4. Dual Priority Queue
// 688ms

#include <iostream>
#include <queue>

using namespace std;

int T;
bool visited[1000001];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> T;

    while (T--)
    {
        int k;
        cin >> k;

        priority_queue<pair<int, int>> maxQ;
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minQ;

        for (int i = 0; i < k; i++)
        {
            char func;
            int n;
            cin >> func >> n;

            if (func == 'I')
            {
                maxQ.push({ n, i });
                minQ.push({ n, i });
                visited[i] = 1;
            }
            else
            {
                if (n == 1)
                {
                    while (!maxQ.empty() && !visited[maxQ.top().second])
                        maxQ.pop();
                    
                    if (!maxQ.empty())
                    {
                        visited[maxQ.top().second] = 0;
                        maxQ.pop();
                    }
                }
                else
                {
                    while (!minQ.empty() && !visited[minQ.top().second])
                        minQ.pop();
                    
                    if (!minQ.empty())
                    {
                        visited[minQ.top().second] = 0;
                        minQ.pop();
                    }
                }
            }
        }

        while (!maxQ.empty() && !visited[maxQ.top().second])
            maxQ.pop();
        while (!minQ.empty() && !visited[minQ.top().second])
            minQ.pop();
        
        if (maxQ.empty() && minQ.empty())
            cout << "EMPTY\n";
        else
            cout << maxQ.top().first << ' ' << minQ.top().first << '\n';
    }
}