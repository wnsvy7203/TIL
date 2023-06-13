// Silver 3. Rotating Queue

#include <iostream>
#include <deque>

using namespace std;

int N, M;
deque<int> nums;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;

    for (int i = 1; i <= N; i++)
        nums.push_back(i);

    int loc;
    int cnt = 0;

    for (int i = 0; i < M; i++)
    {
        cin >> loc;

        if (nums.front() == loc)
            nums.pop_front();
        else
        {
            int idx;

            for (int i = 0; i < nums.size(); i++)
                if (nums[i] == loc)
                    idx = i;
            
            if (nums.size() / 2 < idx)
                while (nums.front() != loc)
                {
                    int end = nums.back();
                    nums.pop_back();
                    nums.push_front(end);
                    cnt++;
                }
            else
                while (nums.front() != loc)
                {
                    int front = nums.front();
                    nums.pop_front();
                    nums.push_back(front);
                    cnt++;
                }
            
            if (nums.front() == loc)
                nums.pop_front();
        }
    }

    cout << cnt;
}