// Silver 2. Coordinates Compression
// 460ms

#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int N;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N;

    vector<int> X(N);

    for (int i = 0; i < N; i++)
        cin >> X[i];
    
    vector<int> Xi(X);
    sort(Xi.begin(), Xi.end());
    Xi.erase(unique(Xi.begin(), Xi.end()), Xi.end());

    for (int i = 0; i < N; i++)
    {
        auto it = lower_bound(Xi.begin(), Xi.end(), X[i]);

        cout << it - Xi.begin() << ' ';
    }
}