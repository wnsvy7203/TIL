// Silver 2. Bertrand's Postulate
// 80ms

#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

vector<int> nums(246913, 0);

void prime()
{
    nums[2] = 1;

    for (int i = 2; i <= 246912; i++)
    {
        bool check = 1;

        for (int j = 2; j <= sqrt(i)+1; j++)
        {
            if (!(i % j))
            {
                check = 0;
                break;
            }
        }

        if (check)
            nums[i] = 1;
    }
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    prime();

    while (1)
    {
        int n;

        cin >> n;

        int cnt = 0;

        if (!n)
            break;
        
        for (int i = n+1; i <= 2*n; i++)
        {
            if (nums[i] == 1)
            {
                cnt++;
            }
        }

        cout << cnt << '\n';
    }
}