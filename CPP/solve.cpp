//

#include <iostream>
#include <queue>
#include <stack>

using namespace std;

int N;
queue<int> que;
stack<int> stk;

int arr[1001];

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;

    int inp;

    while (N--)
    {
        cin >> inp;
        que.push(inp);
    }
    
    int num = 1; // 현재 간식을 받을 학생의 번호
    bool flag = 1;

    while (!que.empty())
    {
        int f = que.front();

        // que front에 있는 학생이 간식을 받을 수 있으면
        if (f == num)
        {
            que.pop(); // 주고 보내
            num++;
        }
        // que front에 있는 학생은 못 받는데,
        else
        {
            // stk top에 있는 학생이 받아서 순서가 맞게 되면
            if (!stk.empty() && stk.top() == num)
            {
                stk.pop();
                num++;
            }
            // 애초에 stk.top보다 크고 줄 수도 없으면 분배 불가능
            else if (!stk.empty() && stk.top() < f)
            {
                flag = 0;
                break;
            }
            else
            {
                que.pop();
                stk.push(f);
            }
        }
    }
    
    while (!stk.empty())
    {
        int t = stk.top();

        if (num == t)
        {
            stk.pop();
            num++;
        }
        else
        {
            flag = 0;
            break;
        }
    }

    if (flag)
        cout << "Nice";
    else
        cout << "Sad";

}