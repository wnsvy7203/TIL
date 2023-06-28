// Silver 3. Rink the Numbers

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int visited[1000001] = {0, };

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    string num, str = "";
    cin >> num;

    int idx = 0;
    for (int i = 1; i < 100000; i++)
    {
        str += to_string(i);
        for (int j = idx; j < idx + to_string(i).size(); j++)
            visited[j] = i;
        idx += to_string(i).size();
    }

    int res = 0;

    for (int i = 0; i < str.size(); i++)
    {
        if (res == num.size())
        {
            cout << visited[i-1];
            break;
        }
        
        if (num[res] == str[i])
            res++;
    }
}