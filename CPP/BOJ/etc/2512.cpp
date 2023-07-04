// Silver 3. Budget

#include <iostream>
#include <algorithm>
#include <numeric>

using namespace std;

int N, M;
int budg[10001];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    
    cin >> N;

    for (int i = 0; i < N; i++)
        cin >> budg[i];
    
    cin >> M;
    
    sort(budg, budg+N);

    int start = 0;
    int end = budg[N-1];
    int sum = 0;
    int cost = 0;

    while (start <= end)
    {
        sum = 0;
        cost = (start + end) / 2;

        for (int i = 0; i < N; i++)
        {
            if (budg[i] < cost)
                sum += budg[i];
            else
                sum += cost;
        }

        if (sum <= M)
            start = cost + 1;
        else
            end = cost - 1;
    }

    cout << end;
}