// Bronze 3. Three Sticks

#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

int main()
{
    int a, b, c;
    
    cin >> a >> b >> c;
    
    vector<int> sticks;
    
    sticks.push_back(a);
    sticks.push_back(b);
    sticks.push_back(c);
    
    sort(sticks.begin(), sticks.end());
    
    if (sticks[0] + sticks[1] > sticks[2])
    {
        cout << accumulate(sticks.begin(), sticks.end(), 0);
    }
    else
    {
        sticks[2] = sticks[0] + sticks[1] - 1;
        
        cout << accumulate(sticks.begin(), sticks.end(), 0);
    }
}