// Silver 5. Sorting Coordinates
// 144ms

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int N;

    cin >> N;

    vector<vector<int>> dots(N, vector<int>(2, 0));

    for (int i = 0; i < N; i++)
    {
        int x, y;

        cin >> x >> y;

        dots[i][0] = x;
        dots[i][1] = y;
    }

    sort(dots.begin(), dots.end());

    for (int i = 0; i < N; i++)
    {
        cout << dots[i][0] << ' ' << dots[i][1] << '\n';
    }
}