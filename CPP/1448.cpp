// Silver 3. Making Triangle

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
    int L[1000001] = {0, };

    cin >> N;

    for (int i = 0; i < N; i++)
        cin >> L[i];
    
    sort(L, L+N, greater<>());

    for (int i = N-3; i >= 0; i++)
    {
        if (L[i] < L[i+1] + L[i+2])
        {
            cout << L[i] + L[i+1] + L[i+2];
            break;
        }
        else if (i == N-3)
            cout << -1;
    }    
}