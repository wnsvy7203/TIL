// Silver 3. Ranking
// 80ms

#include <iostream>
#include <algorithm>

using namespace std;

int N;
int rnk[500001];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N;

    for (int i = 0; i < N; i++)
        cin >> rnk[i];

    sort(rnk, rnk+N);

    long long int ans = 0;

    for (int i = 0; i < N; i++)
        ans += abs((i+1) - rnk[i]);

    cout << ans;
}