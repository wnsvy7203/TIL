// Silver 2. Cutting Trees
// 188ms

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N, M;
    vector<long long int> trees(1000001, 0);

    cin >> N >> M;

    for (int i = 0; i < N; i++)
        cin >> trees[i];
    
    sort(trees.begin(), trees.begin()+N, greater<>());

    int start = 1;
    int end = trees[0];

    while (start <= end)
    {
        int mid = (start + end) / 2;
        long long int height = 0;

        for (int i = 0; i < N; i++)
        {
            if (trees[i] > mid)
                height += trees[i] - mid;
        }

        if (height >= M) start = mid + 1;
        else end = mid - 1;
    }

    cout << end;
}