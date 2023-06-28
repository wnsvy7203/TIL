// Silver 3. Mechanic

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, L;
vector<int> nums;

bool visited[2001] = {0, };

int main()
{
    cin >> N >> L;

    for (int i = 0; i < N; i++)
    {
        int num;
        cin >> num;

        nums.push_back(num);
    }

    sort(nums.begin(), nums.end());

    L -= 1;

    int cnt = 0;

    for (int i = 0; i < N; i++)
    {
        if (!visited[nums[i]])
        {
            for (int j = nums[i]; j <= nums[i]+L; j++)
                visited[j] = 1;
            cnt++;
        }
    }

    cout << cnt;
}