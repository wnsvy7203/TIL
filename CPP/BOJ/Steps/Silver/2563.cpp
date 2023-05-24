// Silver 5. Confetti

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<vector<int>> nums(101, vector<int>(101, 0));

    int N;

    cin >> N;

    for (int i = 0; i < N; i++)
    {
        int a, b;

        cin >> a >> b;

        for (int j = a; j < a+10; j++)
        {
            for (int k = b; k < b+10; k++)
            {
                nums[j][k] += 1;
            }
        }
    }

    int cnt = 0;

    for (int i = 1; i <= 100; i++)
    {
        for (int j = 1; j <= 100; j++)
        {
            if (nums[i][j] != 0)
            {
                cnt += 1;
            }
        }
    }

    cout << cnt;
}