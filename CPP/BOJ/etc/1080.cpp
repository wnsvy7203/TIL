// Silver 1. Procession

#include <iostream>
#include <vector>

using namespace std;

int N, M;

vector<vector<char>> A(51, vector<char>(51, 0));
vector<vector<char>> B(51, vector<char>(51, 0));

void matrix(int x, int y)
{
    for (int i = x; i < x+3; i++)
    {
        for (int j = y; j < y+3; j++)
        {
            if (A[i][j] == '1')
                A[i][j] = '0';
            else
                A[i][j] = '1';
        }
    }
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N >> M;

    

    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            cin >> A[i][j];

    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            cin >> B[i][j];

    int cnt = 0;

    for (int i = 0; i < N-2; i++)
        for (int j = 0; j < M-2; j++)
            if (A[i][j] != B[i][j])
            {
                matrix(i, j);
                cnt++;
            }

    bool flag = 0;

    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            if (A[i][j] != B[i][j])
                flag = 1;

    if (flag) cout << -1;
    else cout << cnt;
}