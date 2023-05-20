// Bronze 2. Blackjack
// 24ms

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int N, M;

    cin >> N >> M;

    vector<int> nums(N);
    vector<int> visit(N);

    for (int i = 0; i < N; i++)
    {
        cin >> nums[i];
    }

    for (int i = 0; i < N-3; i++)
    {
        visit[i] = 0;
    }
    for (int i = N-3; i < N; i++)
    {
        visit[i] = 1;
    }

    vector<int> res;

    do
    {
        int sum = 0;

        for (int i = 0; i < N; i++)
        {
            if (visit[i] != 0)
            {
                sum += nums[i];
            }
        }
        if (sum <= M)
        {
            res.push_back(sum);
        }
    }
    while(next_permutation(visit.begin(), visit.end()));

    int max = *max_element(res.begin(), res.end());

    cout << max;
}