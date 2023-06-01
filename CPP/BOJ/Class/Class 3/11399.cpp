// Silver 4. ATM

#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main()
{
    int N;
    vector<int> time(1005, 0);

    cin >> N;

    for (int i = 1; i <= N; i++)
        cin >> time[i];
    
    sort(time.begin()+1, time.begin()+N+1, greater<>());

    int sum = 0;

    for (int i = 1; i <= N; i++)
        sum += accumulate(time.begin()+i, time.begin()+N+1, 0);

    cout << sum;
}