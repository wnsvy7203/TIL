// Silver 3. Pop the Balloon

#include <iostream>
#include <deque>
#include <algorithm>

using namespace std;

int N;

deque<pair<int, int>> deq;

int main()
{
    cin >> N;

    int num;
    for (int i = 1; i <= N; i++)
    {
        cin >> num;

        deq.push_back(make_pair(num, i));
    }

    while (!deq.empty())
    {
        int front = deq.front().first;
        cout << deq.front().second << ' ';

        deq.pop_front();

        if (deq.empty())
            break;
        
        if (front > 0)
        {
            for (int i = 0; i < front-1; i++)
            {
                deq.push_back(deq.front());
                deq.pop_front();
            }
        }
        else
        {
            for (int i = 0; i < -front; i++)
            {
                deq.push_front(deq.back());
                deq.pop_back();
            }
        }
    }
}
