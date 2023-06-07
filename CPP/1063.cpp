// Silver 3. King

#include <iostream>

using namespace std;

int main()
{
    string king;
    string stone;
    int N;

    pair<char, char> loc_king;
    pair<char, char> loc_stone;

    cin >> king >> stone >> N;

    loc_king.first = king[0];
    loc_king.second = king[1];

    loc_stone.first = stone[0];
    loc_stone.second = stone[1];

    for (int i = 0; i < N; i++)
    {
        string move;

        cin >> move;

        if (move == "R")
        {
            if (loc_king.first != 'H')
            {
                loc_king.first++;

                if (loc_king == loc_stone)
                {
                    loc_stone.first++;

                    if (loc_stone.first == 'I')
                    {
                        loc_king.first--;
                        loc_stone.first--;
                    }
                }
            }
        }
        else if (move == "L")
        {
            if (loc_king.first != 'A')
            {
                loc_king.first--;

                if (loc_king == loc_stone)
                {
                    loc_stone.first--;

                    if (loc_stone.first == 64)
                    {
                        loc_king.first++;
                        loc_stone.first++;
                    }
                }
            }            
        }
        else if (move == "B")
        {
            if (loc_king.second != '1')
            {
                loc_king.second--;

                if (loc_king == loc_stone)
                {
                    loc_stone.second--;

                    if (loc_stone.second == '9')
                    {
                        loc_king.second++;
                        loc_stone.second++;
                    }
                }
            }
        }
        else if (move == "T")
        {
            if (loc_king.second != '8')
            {
                loc_king.second++;

                if (loc_king == loc_stone)
                {
                    loc_stone.second++;
                    
                    if (loc_stone.second == '0')
                    {
                        loc_king.second--;
                        loc_stone.second--;
                    }
                }
            }
        }
        else if (move == "RT")
        {
            if (loc_king.first != 'H' || loc_king.second != '8')
            {
                loc_king.first++;
                loc_king.second++;

                if (loc_king == loc_stone)
                {
                    loc_stone.first++;
                    loc_stone.second++;

                    if (loc_stone.first == 'I' || loc_stone.second == '9')
                    {
                        loc_king.first--;
                        loc_king.second--;

                        loc_stone.first--;
                        loc_stone.second--;
                    }
                }
            }
        }
        else if (move == "LT")
        {
            if (loc_king.first != 'A' || loc_king.second != '8')
            {
                loc_king.first--;
                loc_king.second++;

                if (loc_king == loc_stone)
                {
                    loc_stone.first--;
                    loc_stone.second++;

                    if (loc_stone.first == 64 || loc_stone.second == '9')
                    {
                        loc_king.first++;
                        loc_king.second--;

                        loc_stone.first++;
                        loc_stone.second--;
                    }
                }
            }
        }
        else if (move == "RB")
        {
            if (loc_king.first != 'H' || loc_king.second != '1')
            {
                loc_king.first++;
                loc_king.second--;

                if (loc_king == loc_stone)
                {
                    loc_stone.first++;
                    loc_stone.second--;

                    if (loc_stone.first == 'I' || loc_stone.second == '0')
                    {
                        loc_king.first--;
                        loc_king.second++;

                        loc_stone.first--;
                        loc_stone.second++;
                    }
                }
            }
        }
        else if (move == "LB")
        {
            if (loc_king.first != 'A' || loc_king.second != '1')
            {
                loc_king.first--;
                loc_king.second--;

                if (loc_king == loc_stone)
                {
                    loc_stone.first--;
                    loc_stone.second--;

                    if (loc_stone.first == 64 || loc_stone.second == '0')
                    {
                        loc_king.first++;
                        loc_king.second++;

                        loc_stone.first++;
                        loc_stone.second++;
                    }
                }
            }
        }
    }

    cout << loc_king.first << loc_king.second << '\n' << loc_stone.first << loc_stone.second;
}