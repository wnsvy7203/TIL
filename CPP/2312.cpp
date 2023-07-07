// Silver 3. Restore the Numbers

#include <iostream>
#include <vector>
#include <cmath>
#define MAX 100001

using namespace std;

int T;
int nums[MAX];
vector<int> prime;

void eratos()
{
    nums[0] = -1;
    nums[1] = -1;

    for (int i = 2; i < MAX; i++)
        nums[i] = i;
    
    for (int i = 2; i <= sqrt(MAX); i++)
        if (nums[i] == i)
            for (int j = i*i; j < MAX; j += i)
                if (nums[j] = j)
                    nums[j] = i;

    for (int i = 2; i < MAX; i++)
        if (nums[i] == i)
            prime.push_back(i);
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> T;

    eratos();

    while (T--)
    {
        int N;
        cin >> N;

        for (int i = 0; i < prime.size(); i++)
        {
            int cnt = 0;
            while (!(N%prime[i]))
            {
                cnt++;
                N /= prime[i];

                if (N == 1)
                    break;
            }

            if (cnt)    cout << prime[i] << ' ' << cnt << '\n';

            if (N == 1)
                break;
        }
    }
}