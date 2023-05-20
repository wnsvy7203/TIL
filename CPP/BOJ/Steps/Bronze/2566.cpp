// Brozne 3. Max Value

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int max = -1;

    vector<vector<int>> nums(9, vector<int>(9, 0));

    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            cin >> nums[i][j];

            if (max < nums[i][j])
            {
                max = nums[i][j];
            }
        }
    }

    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            if (nums[i][j] == max)
            {
                cout << max << "\n";
                cout << i+1 << " " << j+1;
                exit(0);
            }
        }
    }
}