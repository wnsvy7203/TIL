// Silver 1. IOIOI
// 52ms

#include <iostream>
#include <vector>

using namespace std;

int N, M;
string S;

int main()
{
    cin >> N >> M >> S;

    int cnt = 0;
    int step = 0;
    int ans = 0;

    while (step < M-1)
    {
        if (S.substr(step, 3) == "IOI")
        {
            cnt++;
            step += 2;

            if (cnt == N)
            {
                ans++;
                cnt--;
            }
        }
        else
        {
            step++;
            cnt = 0;
        }
    }

    cout << ans;
}