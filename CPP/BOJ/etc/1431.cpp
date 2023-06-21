// Silver 3. Serial Number

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
vector<string> serial(51, "");

bool compare(string a, string b)
{
    if (a.length() != b.length())
        return a.length() < b.length();
    else if (a.length() == b.length())
    {
        int cntA = 0;
        int cntB = 0;

        for (int i = 0; i < a.length(); i++)
            if (isdigit(a[i]))
                cntA += int(a[i]) - 48;
        
        for (int i = 0; i < b.length(); i++)
            if (isdigit(b[i]))
                cntB += int(b[i]) - 48;
        
        if (cntA != cntB)
            return cntA < cntB;
    }
    
    return a < b;
}

int main()
{
    cin >> N;

    for (int i = 0; i < N; i++)
        cin >> serial[i];
    
    sort(serial.begin(), serial.begin()+N, compare);

    for (int i = 0; i < N; i++)
        cout << serial[i] << '\n';
}