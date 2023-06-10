// Silver 2. Lost Bracket

#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

int main()
{
    string str;
    vector<string> temp;

    cin >> str;

    string num = "";

    for (int i = 0; i < str.length(); i++)
    {
        if (isdigit(str[i]))
            num += str[i];
        else
        {
            temp.push_back(num);
            string cal = "";
            cal += str[i];

            temp.push_back(cal);
            num = "";
        }
    }
    temp.push_back(num);

    for (int i = 0; i < temp.size(); i++)
        if (temp[i] == "+")
        {
            temp[i+1] = to_string(stoi(temp[i+1]) + stoi(temp[i-1]));
            temp[i-1] = "0";
        }

    queue<int> res;

    int sub = 0;

    for (int i = 0; i < temp.size(); i++)
        if (temp[i] != "-" && temp[i] != "+" && temp[i] != "0")
            res.push(stoi(temp[i]));
        else if (temp[i] == "-")
            sub++;

    int ans = res.front();

    while (sub--)
    {
        res.pop();
        int second = res.front();

        ans -= second;
    }
    
    cout << ans;
}