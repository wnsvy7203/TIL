// Bronze 2. Blackjack

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int N, M;

    cin >> N >> M;

    vector<int> v(N);
    vector<int> temp(N);
    vector<int> visit(N);
    vector<int> res(N);

    for (int i = 0; i < N; i++)
    {
        cin >> v[i];
    }

    for (int i = 0; i < N-3; i++)
    {
        visit[i] = 0;
    }
    for (int i = N-3; i < N; i++)
    {
        visit[i] = 1;
    }

    sort(v.begin(), v.end());

    int sum = 0;

    do
    {
        for (int i = 0; i < N; i++)
        {
            if (visit[i] != 0)
            {
                sum += v[i];
            }
        }

        temp.push_back(abs(sum-M));
        res.push_back(sum);
        
    } while(next_permutation(visit.begin(), visit.end()));

    int min = *min_element(temp.begin(), temp.end());

    for (int i = 0; i < N; i++)
    {
        if (temp[i] == min)
        {
            cout << i;
        }
    }

    cout << res[min];
}