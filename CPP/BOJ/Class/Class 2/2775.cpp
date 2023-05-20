// Bronze 1. President of a Apartment Community
// 4ms

#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

int apt(int k, int n)
{
    vector<vector<int>> apt(15, vector<int>(14, 0));

    for (int i = 0; i < 15; i++)
    {
        for (int j = 0; j < 14; j++)
        {
            if (i == 0)
            {
                apt[i][j] = j + 1;
            }
            else
            {
                apt[i][j] = accumulate(apt[i-1].begin(), apt[i-1].begin()+j+1, 0);
            }
        }
    }

    return apt[k][n-1];
}

int main()
{
    int T;

    cin >> T;

    for (int t = 0; t < T; t++)
    {
        int k, n;

        cin >> k >> n;

        cout << apt(k, n) << '\n';
    }
}