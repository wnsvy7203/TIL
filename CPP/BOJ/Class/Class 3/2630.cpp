// Silver 2. Making Confetti

#include <iostream>
#include <vector>

using namespace std;

int white = 0;
int blue = 0;
vector<vector<int>> con(128, vector<int>(128, 0));

void color(int r, int c, int n)
{
    int start = con[r][c];

    for (int i = r; i < r+n; i++)
        for (int j = c; j < c+n; j++)
            if (con[i][j] != start)
            {
                for (int a = 0; a < 2; a++)
                    for (int b = 0; b < 2; b++)
                        color(r+a*(n/2), c+b*(n/2), n/2);
                return;
            }
    
    if (!start) white++;
    else blue++;
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    int N;
    cin >> N;


    for (int i = 0; i < N; i++)
        for (int j = 0; j < N; j++)
            cin >> con[i][j];
    
    color(0, 0, N);

    cout << white << '\n' << blue;
}
