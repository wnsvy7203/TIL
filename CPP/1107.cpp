// Gold 5. Remote Controller

#include <iostream>
#include <string>

using namespace std;

int N, M;
int err[10] = {0, };

int main()
{
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

        for (int j = 0; j < str.size(); j++)
        {
            if (err[str[i] - 48] == 1)
                break;
            else if (j == str.size()-1)
                btn = min(btn, abs(i - N) + str.size());
        }
    }

    cout << btn;
}