// Silver 3. Making Maze

#include <iostream>
#include <vector>

using namespace std;

int L;
string M;

bool maze[101][101];

int dr[4] = {1, 0, -1, 0};
int dc[4] = {0, -1, 0, 1};

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> L >> M;

    int r = 50;
    int c = 50;
    maze[r][c] = 1;

    int d = 0;
    for (int i = 0; i < M.length(); i++)
    {
        switch(M[i])
        {
            case 'R':
                d = (d+1)%4;
                break;
            case 'L':
                if (!d) d = 3;
                else d = (d-1)%4;
                break;
            case 'F':
                r += dr[d];
                c += dc[d];
                maze[r][c] = 1;
                break;
        }
    }

    int sr, sc, er, ec;
    sr = sc = 100;
    er = ec = 0;

    for (int i = 0; i < 101; i++)
    {
        for (int j = 0; j < 101; j++)
        {
            if (maze[i][j])
            {
                if (i < sr) sr = i;
                if (j < sc) sc = j;
                if (i > er) er = i;
                if (j > ec) ec = j;
            }
        }
    }
    
    for (int i = sr; i <= er; i++)
    {
        for (int j = sc; j <= ec; j++)
        {
            if (maze[i][j]) cout << '.';
            else cout << '#';
        }
        cout << '\n';
    }
}