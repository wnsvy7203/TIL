// Silver 3. Making Pellindrom

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

string str;

int main()
{
    cin >> str;

    int N = str.length();
    vector<char> temp(N, ' ');

    for (int i = 0; i < N; i++)
        temp[i] = str[i];

    sort(temp.begin(), temp.end());

    str = "";

    for (int i = 0; i < N; i++)
        str += temp[i];
    
    bool flag = 1;

    for (int i = 0; i < N/2; i++)
        if (str[i] != str[N-1-i])
            for (int j = i+1; j < N; j++)
            {
                if (str[i] == str[j])
                {
                    char c = str[j];
                    str[j] = str[N-1-i];
                    str[N-1-j] = c;
                    break;
                }
                flag = 0;
            }


    if (!flag) cout << "I'm Sorry Hansoo";
    else cout << str;

}