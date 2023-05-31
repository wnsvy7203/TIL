// Silver 4. Finding Number
// 52ms

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int N, M;

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N;

    vector<int> A(100001, 0);

    for (int i = 0; i < N; i++)
        cin >> A[i];
    
    sort(A.begin(), A.begin()+N);

    cin >> M;
    
    for (int i = 0; i < M; i++)
    {
        int num;

        cin >> num;

        int start = 0;
        int end = N-1;
        bool flag = 0;

        while (start <= end)
        {
            int mid = (start + end) / 2;

            if (num < A[mid])
                end = mid - 1;
            else if (num > A[mid])
                start = mid + 1;
            else
            {
                flag = 1;
                break;
            }
        }

        if (flag) cout << 1 << '\n';
        else cout << 0 << '\n';
    }
}