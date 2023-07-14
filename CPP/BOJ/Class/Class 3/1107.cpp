// Gold 5. Remote Controller
// 24ms

#include <iostream>
#include <string>

using namespace std;

int N, M;
int err[10] = {0, };

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> N >> M;

    for (int i = 0; i < M; i++)
    {
        int num;

        cin >> num;

        err[num] = 1;
    }

    int btn = abs(100 - N);

    for (int i = 0; i < 1000001; i++)
    {
        string str = to_string(i);
        int len = str.size();

        for (int j = 0; j < len; j++)
        {
            if (err[str[j] - 48] == 1)
                break;
            else if (j == str.size()-1)
                btn = min(btn, abs(i - N) + len);
        }
    }

    cout << btn;
}