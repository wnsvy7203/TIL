// Silver 4. Balanced World
// 144ms

#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main()
{
    string str;

    while (1)
    {
        stack<char> stk;

        bool check = 1;

        getline(cin, str);

        if (str == ".")
            break;
        else if (str == "")
            continue;
        
        for (int i = 0; i < str.length(); i++)
        {
            switch (str[i])
            {
                case '(':
                    stk.push(str[i]);
                    break;
                case '[':
                    stk.push(str[i]);
                    break;
                case ')':
                    if (stk.empty())
                    {
                        check = 0;
                        break;
                    }
                    else
                    {
                        if (stk.top() == '(')
                        {
                            stk.pop();
                            break;
                        }
                        else
                        {
                            check = 0;
                            break;
                        }
                    }
                case ']':
                    if (stk.empty())
                    {
                        check = 0;
                        break;
                    }
                    else
                    {
                        if (stk.top() == '[')
                        {
                            stk.pop();
                            break;
                        }
                        else
                        {
                            check = 0;
                            break;
                        }
                    }
            }
        }

        if (!check)
            cout << "no" << '\n';
        else
        {
            if (stk.empty())
                cout << "yes" << '\n';
            else
                cout << "no" << '\n';
        }
    }
}