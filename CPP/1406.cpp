// Silver 2. Editor
// 40ms

#include <iostream>
#include <string>
#include <stack>

using namespace std;

string base;
int N;
char func;
stack<char> stk_left;
stack<char> stk_right;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> base >> N;

    for (int i = 0; i < base.size(); i++)
        stk_left.push(base[i]);

    while (N--)
    {
        cin >> func;
        char word;

        switch (func)
        {
            case 'P':
            {
                cin >> word;
                stk_left.push(word);
                break;
            }
            case 'L':
            {
                if (!stk_left.empty())
                {
                    stk_right.push(stk_left.top());
                    stk_left.pop();
                }
                break;
            }
            case 'D':
            {
                if (!stk_right.empty())
                {
                    stk_left.push(stk_right.top());
                    stk_right.pop();
                }
                break;
            }
            case 'B':
            {
                if (!stk_left.empty())
                    stk_left.pop();
                break;
            }
        }
    }

    while (!stk_left.empty())
    {
        stk_right.push(stk_left.top());
        stk_left.pop();
    }
    
    while (!stk_right.empty())
    {
        cout << stk_right.top();
        stk_right.pop();
    }
}