// Silver 3. King

#include <iostream>

using namespace std;

string king;
string stone;
int N;

int main()
{
    cin >> king >> stone >> N;

    while (N--)
    {
        string move;

        cin >> move;

        if (move[0] == 'R')
        {
            if (king[0] + 1 == stone[0] && king[1] == stone[1])
            {
                if (stone[0] + 1 > 'H')
                    continue;
                else
                {
                    king[0]++;
                    stone[0]++;
                }
            }
            else
            {
                if (king[0] + 1 > 'H')
                    continue;
                else
                    king[0]++;
            }
        }
        else if (move[0] == 'L')
        {
            if (king[0] - 1 == stone[0] && king[1] == stone[1])
            {
                if (stone[0] - 1 < 'A')
                    continue;
                else
                {
                    king[0]--;
                    stone[0]--;
                }
            }
            else
            {
                if (king[0] - 1 < 'A')
                    continue;
                else
                    king[0]--;
            }
        }
        else if (move[0] == 'B')
        {
            if (king[1] - 1 == stone[1] && king[0] == stone[0])
            {
                
            }
        }
    }
}