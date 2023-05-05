// Bronze 4. Three dices

#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int dice[3] = { 0 };
    
    for (int i = 0; i < 3; i++)
    {
        cin >> dice[i];
    }
    
    if (dice[0] == dice[1] && dice[0] == dice[2])
    {
        cout << dice[0] * 1000 + 10000;
    }
    else if (dice[0] == dice[1])
    {
        cout << dice[0] * 100 + 1000;
    }
    else if (dice[0] == dice[2])
    {
        cout << dice[0] * 100 + 1000;
    }
    else if (dice[1] == dice[2])
    {
        cout << dice[1] * 100 + 1000;
    }
    else
    {
        int *max = max_element(dice, dice+3);
        cout << *max * 100;
    }
}