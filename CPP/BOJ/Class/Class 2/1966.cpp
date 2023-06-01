// Silver 3. Printer Queue

#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int main()
{
    int T;

    cin >> T;

    while (T--)
    {
        int N, M;

        cin >> N >> M;

        queue<pair<int, int>> que;
        priority_queue<int> pque;

        for (int i = 0; i < N; i++)
        {
            int doc;
            cin >> doc;

            que.push({ doc, i });
            pque.push(doc);
        }

        int cnt = 0;

        while (!que.empty())
        {
            int val = que.front().first;
            int idx = que.front().second;

            que.pop();

            if (pque.top() == val)
            {
                pque.pop();
                cnt++;

                if (idx == M)
                {
                    cout << cnt << '\n';
                    break;
                }
            }
            else que.push({ val, idx });
        }
    }
}