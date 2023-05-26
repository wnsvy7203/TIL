// Silver 5. Sorting Coordinates 2
// 128ms

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

        dots[i][0] = y;
        dots[i][1] = x;
    }

    sort(dots.begin(), dots.end());

    for (int i = 0; i < N; i++)
    {
        cout << dots[i][1] << ' ' << dots[i][0] << '\n';
    }
}
