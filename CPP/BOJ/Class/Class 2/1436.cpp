// Silver 5. Movie Director Shawm
// 476ms

#include <iostream>
#include <string>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int N;

    cin >> N;

    int cnt = 0;
    int num = 666;

    while (1)
    {
        for (int i = 0; i <= to_string(num).length() - 3; i++)
        {
            if (to_string(num).substr(i, 3) == "666")
            {
                cnt++;
                break;
            }
        }

        if (cnt == N)
        {
            cout << num;
            break;
        }
        
        num++;
    }
}