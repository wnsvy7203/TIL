// Silver 4. Right Array

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int N;

    cin >> N;

    vector<int> seq(N);

    for (int i = 0; i < N; i++)
        cin >> seq[i];

    sort(seq.begin(), seq.end());

    int ans = 1;
    for (int i = 0; i < N; i++)
    {
        int k = 1;
        for (int j = i+1; j < i+5; j++)
        {
            if (seq[j] - seq[i] < 5 && seq[j] - seq[i] > 0)
                k++;
        }

        ans = max(ans, k);
    }

    if (ans >= 5)
        cout << 0;
    else
        cout << 5 - ans;
}
