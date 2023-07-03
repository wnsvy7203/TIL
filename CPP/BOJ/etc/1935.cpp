// Silver 3. Postfix Notation2

#include <iostream>
#include <stack>
#include <cmath>

using namespace std;

int N;
string str;
int nums[26] = {0, };
stack<double> stk;

int main()
{
    cin >> N >> str;

    for (int i = 0; i < N; i++)
        cin >> nums[i];
    
    for (int i = 0; i < str.length(); i++)
    {
        if (str[i] >= 65 && str[i] <= 90)
            stk.push(nums[str[i]-65]);
        else
        {
            switch (str[i])
            {
                case '+':
                {
                    double second = stk.top();
                    stk.pop();
                    double first = stk.top();
                    stk.pop();

                    double res = first + second;
                    stk.push(res);
                    break;
                }
                case '-':
                {
                    double second = stk.top();
                    stk.pop();
                    double first = stk.top();
                    stk.pop();

                    double res = first - second;
                    stk.push(res);
                    break;
                }
                case '*':
                {
                    double second = stk.top();
                    stk.pop();
                    double first = stk.top();
                    stk.pop();

                    double res = first * second;
                    stk.push(res);
                    break;
                }
                case '/':
                {
                    double second = stk.top();
                    stk.pop();
                    double first = stk.top();
                    stk.pop();

                    double res = first / second;
                    stk.push(res);
                    break;
                }
            }
        }
    }

    double ans = stk.top();

    cout.precision(2);
    cout << fixed << ans;
}