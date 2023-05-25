// Silver 2. Stack Sequence
// 56ms

#include <iostream>
#include <stack>
#include <queue>

using namespace std;

int main()
{
    int n;

    cin >> n;

    stack<int> stk;
    queue<char> cal;

    bool flag = 1;

    int cnt = 0;

    stk.push(cnt);

    while (n--)
    {
        int a;

        cin >> a;

        while (cnt < a)
        {
            cnt++;
            stk.push(cnt);
            cal.push('+');
        }

        if (stk.top() == a)
        {
            stk.pop();
            cal.push('-');
        }
        else
        {
            flag = 0;
            break;
        }
    }

    if (flag)
    {
        while (!cal.empty())
        {
            cout << cal.front() << '\n';
            cal.pop();
        }
    }
    else
        cout << "NO";
}