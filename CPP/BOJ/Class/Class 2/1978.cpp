// Bronze 2. Finding Prime Numbers

#include <iostream>

using namespace std;

int N;

int main()
{
    cin >> N;

    int nums[1005] = {};

    for (int i = 0; i < N; i++)
    {
        cin >> nums[i];
    }

    int cnt = 0;

    for (int i = 0; i < N; i++)
    {
        if (nums[i] == 1)
        {
            continue;
        }
        else if (nums[i] == 2)
        {
            cnt++;
        }
        else
        {
            bool check = 0;
            
            for (int j = 2; j <= nums[i]-1; j++)
            {

                if (nums[i] % j == 0)
                {
                    check = 1;
                    break;
                }
            }

            if (check == 0)
            {
                cnt++;
            }
        }
    }

    cout << cnt;
}