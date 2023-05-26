// Silver 4. re-Coloring the Chess Board

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
    int N, M;

    cin >> N >> M;

    vector<vector<char>> board(N, vector<char>(M, 0));

    for (int i = 0; i < N; i++)
    {
        string str;

        cin >> str;

        for (int j = 0; j < M; j++)
            board[i][j] = str[j];
    }

    vector<vector<int>> num;

    for (int i = 0; i <= N-8; i++)
    {
        for (int j = 0; j <= M-8; j++)
        {
            vector<int> temp(2, 0);
            
            temp[0] = i;
            temp[1] = j;

            num.push_back(temp);
        }
    }

    int ans = 64;

    for (int i = 0; i < num.size(); i++)
    {
        int cntW, cntB = 0;

        for (int j = num[i][0]; j < num[i][0]+8; j++)
        {
            for (int k = num[i][1]; k < num[i][1]+8; k++)
            {
                if ((j + k) % 2)
                {
                    if (board[j][k] == 'B')
                        cntB++;
                }                
                else
                {
                    if (board[j][k] == 'W')
                        cntB++;
                }

                if ((j + k) % 2)
                {
                    if (board[j][k] == 'W')
                        cntW++;
                }
                else
                {
                    if (board[j][k] == 'B')
                        cntW++;
                }
            }
        }

        if (ans > cntB)
            ans = cntB;

        if (ans > cntW)
            ans = cntW;
    }

    cout << ans;
}