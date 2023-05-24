// Bronze 1. Divisor

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int cnt;

    cin >> cnt;

    vector<int> divisor(1000005, 0);

    for (int i = 0; i < cnt; i++)
    {
        cin >> divisor[i];
    }

    sort(divisor.begin(), divisor.begin()+cnt);

    cout << divisor[0] * divisor[cnt-1];
}