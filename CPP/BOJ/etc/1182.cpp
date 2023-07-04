// Silver 4. Sum of 

#include <iostream>
#include <algorithm>

using namespace std;

int N, S, ans;
int nums[20];

void dfs(int idx, int tmp)
{
    if (idx == N)
        return;
    if (tmp + nums[idx] == S)
        ans++;
    
    dfs(idx+1, tmp);
    dfs(idx+1, tmp+nums[idx]);
}

int main()
{
    cin >> N >> S;

    for (int i = 0; i < N; i++)
        cin >> nums[i];

    dfs(0, 0);
    
    cout << ans;
}