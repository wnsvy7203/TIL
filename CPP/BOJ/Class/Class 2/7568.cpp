// Silver 5. Big Guy

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int N;

    cin >> N;

    vector<vector<int>> S(N, vector<int>(2, 0));

    for (int i = 0; i < N; i++)
    {
        int a, b;

        cin >> a >> b;

        S[i][0] = a;
        S[i][1] = b;

    }

    for (int i = 0; i < N; i++)
    {
        int rank = 1;

        for (int j = 0; j < N; j++)
        {
            if (S[i][0] < S[j][0] && S[i][1] < S[j][1])
                rank++;
        }
        
        cout << rank << " ";
    }
}