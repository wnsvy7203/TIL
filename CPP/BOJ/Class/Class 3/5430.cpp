// Gold 5. AC
// 56ms

#include <iostream>
#include <deque>
#include <string>
#include <algorithm>

using namespace std;

int T;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> T;

    string func;
    int n;
    string arr;

    while (T--)
    {
        cin >> func >> n >> arr;

        deque<int> deq;
        
        string num = "";
        for (int i = 0; i < arr.size(); i++)
        {
            if (isdigit(arr[i]))
                num += arr[i];
            else
            {
                if (!num.empty())
                {
                    deq.push_back(stoi(num));
                    num = "";
                }
            }
        }

        bool rev = 0;
        bool flag = 1;

        for (int i = 0; i < func.size(); i++)
        {
            if (func[i] == 'R')
                if (rev) rev = 0;
                else rev = 1;
            else if (func[i] == 'D')
            {
                if (!deq.empty())
                    if (rev % 2)
                        deq.pop_back();
                    else
                        deq.pop_front();
                else
                {
                    flag = 0;
                    cout << "error" << '\n';
                    break;
                }
            }
        }

        if (flag)
        {
            if (rev % 2)
                reverse(deq.begin(), deq.end());
            
            cout << '[';
            while (!deq.empty())
            {
                if (deq.size() > 1)
                {
                    cout << deq.front() << ',';
                    deq.pop_front();
                }
                else
                {
                    cout << deq.front();
                    deq.pop_front();
                }
            }
            cout << ']' << '\n';
        }
    }
}