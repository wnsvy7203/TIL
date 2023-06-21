// Silver 3. Making Triangle
// 176ms

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N;
    
    vector<int> L(N, 0);

    for (int i = 0; i < N; i++)
        cin >> L[i];
    
    sort(L.begin(), L.end(), greater<>());

    for (int i = 0; i <= N-3; i++)
    {
        if (L[i] < L[i+1] + L[i+2])
        {
            cout << L[i] + L[i+1] + L[i+2];
            return 0;
        }
    }

    cout << -1;
}