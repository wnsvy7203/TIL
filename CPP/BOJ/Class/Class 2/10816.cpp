// Silver 4. Digit Card 2
// 296ms

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, M;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N;

    vector<int> card(N, 0);
    vector<int> res(20000002, 0);

    for (int i = 0; i < N; i++)
    {
        cin >> card[i];

        res[card[i]+10000000]++;
    }

    cin >> M;

    vector<int> check(M, 0);

    for (int i = 0; i < M; i++)
        cin >> check[i];

    for (int i = 0; i < M; i++)
        cout << res[check[i]+10000000] << ' ';
}