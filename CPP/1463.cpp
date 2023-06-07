// Silver 3. Making 1

#include <iostream>
#include <vector>

using namespace std;

vector<int> cal(1000001, 0);

void calculate()
{
    for (int i = 2; i <= 1000000; i++)
    {
        if (!(i % 3) && !(i % 2))
            cal[i] = min(min(cal[i/3]+1, cal[i/2]+1), cal[i-1]+1);
        else if (!(i % 3) && (i % 2))
            cal[i] = min(cal[i/3]+1, cal[i-1]+1);
        else if ((i % 3) && !(i % 2))
            cal[i] = min(cal[i/2]+1, cal[i-1]+1);
        else cal[i] = cal[i-1]+1;
    }
}

int main()
{
    int N;

    cin >> N;

    calculate();

    cout << cal[N];
}